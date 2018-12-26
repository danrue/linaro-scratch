#!/usr/bin/python3

import base64
import boto3
from pprint import pprint
import sys
import time


class spotBuilder:
    def __init__(
        self,
        image_id,
        ec2_key_name,
        security_groups,
        user_data,
        image_root_device="/dev/sda1",
        volume_size_gb=20,
        ec2_type="c5.2xlarge",
        spot_price="0.30",
        spot_timeout=180,
    ):
        """
            Do a build, as defined in user_data, on a spot instance in AWS.

            image_id: AMI ID
            ec2_key_name: EC2 SSH key name
            security_groups: EC2 security groups (list)
            user_data: User data script - byte string
            image_root_device: root device path in AMI
            volume_size_gb: EBS volume size in GB (int)
            ec2_type: EC2 instance type
            spot_price: Max spot price (string)
            spot_timeout: Max seconds to wait for spot request (int)

        """
        start = time.time()
        self.image_id = image_id
        self.ec2_key_name = ec2_key_name
        self.security_groups = security_groups

        self.user_data = user_data
        self.image_root_device = image_root_device
        self.volume_size_gb = volume_size_gb
        self.ec2_type = ec2_type
        self.spot_price = spot_price
        self.spot_timeout = spot_timeout

        self.client = boto3.client("ec2")

        self.instance_id = self.submit_spot_request()
        self.wait_for_instance()
        end = time.time()
        print("Build complete ({} seconds)".format(int(end-start)))

    def submit_spot_request(self):
        """ Submits a spot request, and returns an instance id """
        print("Submitting spot instance request")
        response = self.client.request_spot_instances(
            InstanceCount=1,
            LaunchSpecification={
                # "IamInstanceProfile": {
                #    "Arn": "arn:aws:iam::123456789012:instance-profile/my-iam-role"
                # },
                "BlockDeviceMappings": [
                    {
                        "DeviceName": self.image_root_device,
                        "Ebs": {"VolumeSize": self.volume_size_gb},
                    }
                ],
                "ImageId": self.image_id,
                "InstanceType": self.ec2_type,
                "KeyName": self.ec2_key_name,
                "SecurityGroupIds": self.security_groups,
                "UserData": base64.b64encode(self.user_data).decode("utf-8"),
            },
            SpotPrice=self.spot_price,
            Type="one-time",
        )

        request_id = response["SpotInstanceRequests"][0]["SpotInstanceRequestId"]

        waiter = self.client.get_waiter("spot_instance_request_fulfilled")
        print("Spot instance request submitted.")
        start = time.time()
        waiter.wait(
            SpotInstanceRequestIds=[request_id],
            WaiterConfig={"Delay": 5, "MaxAttempts": 80},
        )
        end = time.time()
        print("Spot instance request fulfilled ({} seconds)".format(int(end-start)))

        status = self.client.describe_spot_instance_requests(
            SpotInstanceRequestIds=[request_id]
        )["SpotInstanceRequests"][0]
        if status["State"] == "failed":
            print("Spot instance request failed")
            pprint(status["Status"])
            sys.exit(1)

        assert status["State"] == "active", "Error, state is not 'active': {}".format(
            status["Status"]
        )

        # Wait for instance
        instance_id = status.get("InstanceId", None)
        instance_ip = status.get("PublicIpAddress", None)
        assert instance_id, "Error, InstanceId not found: {}".format(status)
        print("Instance {} launched at {}".format(instance_id, instance_ip))
        return instance_id

    def wait_for_instance(self):
        waiter = self.client.get_waiter("instance_running")
        print("Waiting until instance is running")
        start = time.time()
        waiter.wait(
            InstanceIds=[self.instance_id], WaiterConfig={"Delay": 5, "MaxAttempts": 80}
        )
        end = time.time()
        print("Instance is running ({} seconds)".format(int(end-start)))

        waiter = self.client.get_waiter("instance_terminated")
        print("Waiting until instance is terminated")
        start = time.time()
        waiter.wait(
            InstanceIds=[self.instance_id],
            WaiterConfig={"Delay": 15, "MaxAttempts": 80},
        )
        end = time.time()
        print("Instance terminated ({} seconds)".format(int(end-start)))



if __name__ == "__main__":
    # Need a terraform to launch prerequisites
    # - instance-profile

    USER_DATA = b"""#!/bin/sh
    set -ex
    curl -fsSL 'https://github.com/mrchapp.keys' -o keys
    cat keys >> /home/ubuntu/.ssh/authorized_keys
    curl -fsSL 'https://gist.githubusercontent.com/danrue/5595ddb3ed47ec9d3a4cb0ba0f552c2d/raw/gistfile1.txt' -o setup.sh
    curl -fsSL 'https://gist.githubusercontent.com/danrue/d2260630ec6943706f6e3ae9d7934450/raw/gistfile1.txt' -o build.sh
    sh setup.sh > setup-stdout.out 2> setup-stderr.out
    su ubuntu -c 'sh build.sh' > build-stdout.out 2> build-stderr.out
    shutdown -h now
    """

    build = spotBuilder(
        image_id="ami-0ac019f4fcb7cb7e6",  # ubuntu 18.04 amd64
        ec2_key_name="xps",
        security_groups=[
            "sg-8b9514f6",
            "sg-bea120c3",
            "sg-c4c356be",
            "sg-c4c356be",
            "sg-d10590ab",
        ],
        user_data=USER_DATA,
        image_root_device="/dev/sda1",
        volume_size_gb=20,
        ec2_type="c5.2xlarge",
        spot_price="0.30",
        spot_timeout=180,
    )

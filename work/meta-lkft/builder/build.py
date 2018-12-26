#!/usr/bin/python3

import base64
import boto3

# Need a terraform to launch prerequisites
# - instance-profile

AMI = "ami-0ac019f4fcb7cb7e6"
TYPE = "c5.2xlarge"
KEY_NAME = "xps"
VOLUME_SIZE = "30"
AVAILABILITY_ZONE = "us-east-1c"
SECURITY_GROUPS = [
    "sg-8b9514f6",
    "sg-bea120c3",
    "sg-c4c356be",
    "sg-c4c356be",
    "sg-d10590ab",
]
SPOT_PRICE = "0.30"

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


client = boto3.client("ec2")
response = client.request_spot_instances(
    InstanceCount=1,
    LaunchSpecification={
        # "IamInstanceProfile": {
        #    "Arn": "arn:aws:iam::123456789012:instance-profile/my-iam-role"
        # },
        "ImageId": AMI,
        "InstanceType": TYPE,
        "KeyName": KEY_NAME,
        # "Placement": {"AvailabilityZone": AVAILABILITY_ZONE},
        "SecurityGroupIds": SECURITY_GROUPS,
        "UserData": base64.b64encode(USER_DATA).decode('utf-8'),
    },
    SpotPrice=SPOT_PRICE,
    Type="one-time",
)

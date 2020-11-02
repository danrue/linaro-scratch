import json

repos = [
    "drue/foo",
    "drue/bar",
    "drue/baz",
    "drue/biz",
]

policy = {
    "Statement": [
        {
            "Action": [
                "ecr:GetDownloadUrlForLayer",
                "ecr:BatchGetImage"
            ],
            "Effect": "Allow",
            "Principal": {
                "AWS": "*"
            }
        }
    ],
    "Version": "2012-10-17"
}

resources = {}
for repo in repos:
    safe_name = repo.replace('/', '')
    resources[safe_name] = {
        "Properties": {
            "RepositoryName": repo,
            "RepositoryPolicyText": policy,
        },
        "Type": "AWS::ECR::Repository"
    }

template = {
    "Resources": resources
}

print(json.dumps(template, indent=4, sort_keys=True))

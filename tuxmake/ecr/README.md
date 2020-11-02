python gen_cfn.py > ecr-stack.json
cfn-lint ecr-stack.json
aws cloudformation deploy --stack-name drue-ecr --template-file ecr-stack.json

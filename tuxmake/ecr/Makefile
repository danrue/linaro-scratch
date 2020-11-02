deploy: ecr-stack.json lint
	aws cloudformation deploy --stack-name drue-ecr --template-file ecr-stack.json

ecr-stack.json:
	python3 gen_cfn.py > ecr-stack.json

lint: ecr-stack.json
	cfn-lint ecr-stack.json

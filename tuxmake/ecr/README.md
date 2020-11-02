```
$ make
python3 gen_cfn.py > ecr-stack.json
cfn-lint ecr-stack.json
aws cloudformation deploy --stack-name drue-ecr --template-file ecr-stack.json

Waiting for changeset to be created..

No changes to deploy. Stack drue-ecr is up to date
```


```
python gen_cfn.py > ecr-stack.json
cfn-lint ecr-stack.json
aws cloudformation deploy --stack-name drue-ecr --template-file ecr-stack.json
```


Create a bunch of ECRs for tuxmake. Given a list of docker repos, create them
all using a persistent cloudformation stack.

Requires python and the AWS v2 cli.

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


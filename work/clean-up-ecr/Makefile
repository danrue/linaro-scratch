del.sh: repos.txt
	sh gen_del.sh | sort | uniq > del.sh

repos.txt:
	aws ecr describe-repositories | jq -r ".repositories[].repositoryName" > repos.txt

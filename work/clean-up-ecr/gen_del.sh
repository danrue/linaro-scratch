for repo in $(cat repos.txt); do
    for imageid in $(aws ecr list-images --repository-name ${repo} | jq -r ".imageIds|.[]|.imageDigest"); do
        echo aws ecr batch-delete-image --repository-name ${repo} --image-ids imageDigest=${imageid}
    done
done

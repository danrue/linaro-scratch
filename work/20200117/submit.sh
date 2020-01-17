GIT_REPO=https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git
LATEST_SHA=ab7541c3addd344939e76d0636da0048ce24f2db
GIT_BRANCH=master
REPO_NAME=mainline

build_process=pass # or "fail"
git_commit=$(jq -r .git_sha build.json)
git_describe=$(jq -r .git_describe build.json)
job_id=$(date +%s)
squad_build="linux-stable-rc-5.1-oe"
arch="x86"
build_name="build-x86-gcc-9"

curl \
    --header "Auth-Token: ${SQUAD_TOKEN}" \
    --form tests="{\"build/build_process\": \"${build_process}\"}" \
    --form log=@build.log \
    --form metadata="
        {
            \"job_id\": \"${build_name}\",
            \"git branch\": \"${GIT_BRANCH}\",
            \"git repo\": \"${GIT_REPO}\",
            \"git commit\": \"${git_commit}\",
            \"git describe\": \"${git_describe}\"
        }" \
    https://staging-qa-reports.linaro.org/api/submit/lkft/${squad_build}/${git_describe}/${arch}

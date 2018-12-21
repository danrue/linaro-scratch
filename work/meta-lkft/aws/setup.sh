apt-get install -y --no-install-recommends nfs-common
mkdir /oe
mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport fs-e72a9e06.efs.us-east-1.amazonaws.com:/ /oe
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -                                                      
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"                          
apt-get update
apt-get install -y docker-ce
usermod -aG docker ubuntu

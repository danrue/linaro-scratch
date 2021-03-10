# Delete all images from ECR

Usage: Run `make` to discover all repositories and images from ECR, and
generate a `del.sh` file which will contain a delete command for each image.

Running `make` is harmless, but running `del.sh` will destroy data (and lots of
it!)

mkdir -p grafana.linaro.org-backup
docker run --rm -it --name grafana-backup-tool \
   -e GRAFANA_TOKEN=$(cat $HOME/.config/grafana_key) \
   -e GRAFANA_URL=https://grafana.linaro.org \
   -v $(pwd)/grafana.linaro.org-backup:/opt/grafana-backup-tool/_OUTPUT_  \
   ysde/docker-grafana-backup-tool

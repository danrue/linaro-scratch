mkdir -p grafana

curl -s -H "Authorization: Bearer $(cat $HOME/.config/grafana_key)" 'https://grafana.linaro.org/render/d-solo/2co7gfmZk/lkft?orgId=1&var-group=lkft&var-branch=All&from=1497987169327&to=1561059169328&panelId=9&width=1000&height=500&tz=America%2FChicago' --output grafana/total_tests.png
curl -s -H "Authorization: Bearer $(cat $HOME/.config/grafana_key)" 'https://grafana.linaro.org/render/d-solo/2co7gfmZk/lkft?orgId=1&var-group=lkft&var-branch=All&from=1497987240920&to=1561059240920&panelId=11&width=1000&height=500&tz=America%2FChicago' --output grafana/total_tests_by_category.png

cat << EOF > grafana/index.html
<head></head>
<body>
<img src="total_tests.png" />
<br />
<img src="total_tests_by_category.png" />
</body>
EOF

rsync -av grafana people.linaro.org:public_html/


mkdir -p grafana

curl -H "Authorization: Bearer $(cat $HOME/.config/grafana_key)" 'https://grafana.linaro.org/render/d-solo/2co7gfmZk/lkft?tab=queries&orgId=1&var-group=lkft&var-branch=All&panelId=13&width=600&height=200' --output grafana/over_x_tests_run.png
curl -H "Authorization: Bearer $(cat $HOME/.config/grafana_key)" 'https://grafana.linaro.org/render/d-solo/2co7gfmZk/lkft?tab=queries&orgId=1&var-group=lkft&var-branch=All&from=1497989364226&panelId=11&width=1000&height=500' --output grafana/tests_run_simple.png
curl -H "Authorization: Bearer $(cat $HOME/.config/grafana_key)" 'https://grafana.linaro.org/render/d-solo/2co7gfmZk/lkft?orgId=1&var-group=lkft&var-branch=All&from=1497987169327&to=1561059169328&panelId=9&width=1000&height=500&tz=America%2FChicago' --output grafana/total_tests.png
curl -H "Authorization: Bearer $(cat $HOME/.config/grafana_key)" 'https://grafana.linaro.org/render/d-solo/2co7gfmZk/lkft?orgId=1&var-group=lkft&var-branch=All&from=1497987240920&to=1561059240920&panelId=11&width=1000&height=500&tz=America%2FChicago' --output grafana/total_tests_by_category.png

cat << EOF > grafana/index.html
<head></head>
<body>
<img src="over_x_tests_run.png" />
<br />
<img src="tests_run_simple.png" />
<br />
<img src="total_tests.png" />
<br />
<img src="total_tests_by_category.png" />
</body>
EOF

rsync -av grafana people.linaro.org:public_html/


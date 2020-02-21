DATE=$(date +%Y-%m-%d)
mkdir -p $DATE
generate_lts_report.py 4.4 > 4.4 &
generate_lts_report.py 4.9 > 4.9 &
generate_lts_report.py --unfinished 4.14 > 4.14 &
generate_lts_report.py --unfinished --build 23320 4.19 > 4.19 & # build v4.19.76-212-g319532606385
generate_lts_report.py 5.2 > 5.2 &
generate_lts_report.py 5.3 > 5.3 &

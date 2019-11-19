DATE=$(date +%Y-%m-%d)
mkdir -p $DATE
generate_lts_report.py --unfinished 4.14 > $DATE/4.14 &
generate_lts_report.py --unfinished --build 23320 4.19 > $DATE/4.19 & # build v4.19.76-212-g319532606385
generate_lts_report.py 5.2 > $DATE/5.2 &
generate_lts_report.py 5.3 > $DATE/5.3 &

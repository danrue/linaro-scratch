DATE=$(date +%Y-%m-%d)
mkdir -p $DATE
generate_lts_report.py 4.4 > $DATE/4.4 &
generate_lts_report.py 4.9 > $DATE/4.9 &
generate_lts_report.py --unfinished 4.14 > $DATE/4.14 &
generate_lts_report.py --unfinished 4.19 > $DATE/4.19 &
generate_lts_report.py 5.2 > $DATE/5.2 &
generate_lts_report.py 5.3 > $DATE/5.3 &

generate_lts_report.py --build 24603 4.4 > 4.4 &
#generate_lts_report.py --build 24608 --force-good 4.9 > 4.9 & # waiting for it to regenerated via --force-report
generate_lts_report.py --unfinished 4.14 > 4.14 &
generate_lts_report.py 4.19 > 4.19 &
generate_lts_report.py --unfinished 5.3 > 5.3 &

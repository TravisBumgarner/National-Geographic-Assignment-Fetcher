
#!/bin/sh
echo $(date) >> bash_cron_log.txt
cd /home/tbumgarner/scripts/nat_geo_assignment_fetch/
/home/tbumgarner/anaconda3/bin/python main.py >> bash_cron_log.txt


#!/bin/sh
echo $(date) >> bash_cron_log.txt
cd /home/pi/Desktop/nat_geo_assignment_fetch
/usr/bin/python3 main.py >> bash_cron_log.txt

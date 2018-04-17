ps -ef | grep manage.py | grep -v grep | awk '{print $2}' | xargs -n 1 kill -9;
nohup python manage.py runserver 0.0.0.0:80 &> run.log &

#!/bin/bash
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
gunicorn -b 0.0.0.0:8000 --pythonpath /home/box/web/ hello:app&
gunicorn -b 0.0.0.0:8080 --pythonpath /home/box/web/ask ask.wsgi&
#sudo ln -s /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
#sudo /etc/init.d/gunicorn restart
#sudo /etc/init.d/mysql start
echo "Ready!"

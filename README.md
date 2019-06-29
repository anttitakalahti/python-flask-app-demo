¯\_(ツ)_/¯ ~/Work/python-flask [master] [tade@zero] > docker build -t python-flask:latest .
¯\_(ツ)_/¯ ~/Work/python-flask [master] [tade@zero] > docker run -p 5000:5000 -e PORT=5000 python-flask


heroku container:push python-flask
heroku container:release python-flask
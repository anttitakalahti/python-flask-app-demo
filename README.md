<<<<<<< HEAD
# This is a small python app to add text to image.

This is an exercise and do not run this in production.

## Build Docker image

¯\_(ツ)_/¯ ~/Work/python-flask [master] [tade@zero] > docker build -t python-flask:latest .
¯\_(ツ)_/¯ ~/Work/python-flask [master] [tade@zero] > docker run -p 5000:5000 -e PORT=5000 python-flask

## Update Heroku Docker image
=======
¯\_(ツ)_/¯ ~/Work/python-flask [master] [tade@zero] > docker build -t python-flask:latest .
¯\_(ツ)_/¯ ~/Work/python-flask [master] [tade@zero] > docker run -p 5000:5000 -e PORT=5000 python-flask

>>>>>>> 7b7f684afbb72e1370e72bcfa1c581e9159390f2

heroku container:push python-flask
heroku container:release python-flask
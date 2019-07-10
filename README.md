<<<<<<< HEAD
# This is a small python app to add text to image.

This is an exercise and do not run this in production.

## Running locally

* docker run -p 5000:5000 -e PORT=5000 -e DATABASE_URL=postgres://$(whoami) python-flask

## Deploy to heroku

* docker build -t python-flask:latest .
* heroku container:push python-flask
* heroku container:release python-flask
* git push heroku master

## Test

* run from PyCharm
* curl -F 'file=@kasi.jpg' http://127.0.0.1:5000/predict


## TODO 

* unit tests
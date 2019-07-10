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

## Test local setup

* run from PyCharm
* curl -F 'file=@kasi.jpg' http://127.0.0.1:5000/predict


## Test live version

* curl -F 'file=@kasi.jpg' https://python-flask-app-demo.herokuapp.com/predict
* curl -F 'file=@kasi.jpg' -F 'label=8' https://python-flask-app-demo.herokuapp.com/store

## TODO 

* unit tests
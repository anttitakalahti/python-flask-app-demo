FROM python:3.7
MAINTAINER Antti Takalahti "antti.takalahti@gmail.com"

ADD . ./opt/
WORKDIR /opt/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN echo "got port: $PORT from Heroku."

ENTRYPOINT ["python"]
CMD ["app.py"]
FROM python:3.7
MAINTAINER Antti Takalahti "antti.takalahti@gmail.com"

ADD . ./opt/
WORKDIR /opt/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]
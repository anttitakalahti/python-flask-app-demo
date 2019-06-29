FROM python:3.7
ADD . ./opt/
WORKDIR /opt/

ARG runtime_port=5000
ENV port_number=$runtime_port

EXPOSE $port_number

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV FLASK_APP /opt/server.py

CMD flask run -p $port_number

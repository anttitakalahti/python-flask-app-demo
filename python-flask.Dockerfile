FROM python:3.7
ADD . ./opt/
WORKDIR /opt/

RUN echo $PORT

ARG PORT=5000
ENV port_number=$PORT

RUN echo $PORT

EXPOSE $port_number

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV FLASK_APP /opt/server.py

CMD flask run -p $port_number

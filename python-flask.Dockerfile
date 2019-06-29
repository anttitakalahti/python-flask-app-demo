FROM python:3.7
ADD . ./opt/
WORKDIR /opt/
EXPOSE 5000

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV FLASK_APP /opt/server.py

# CMD ["flask", "run"]

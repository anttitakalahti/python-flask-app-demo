FROM python:3.7
ADD . ./opt/
WORKDIR /opt/
EXPOSE 5000

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN pwd
RUN ls
RUN ls /opt

CMD ["FLASK_APP=/opt/server.py", "flask", "run"]

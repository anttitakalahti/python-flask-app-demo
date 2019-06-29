FROM python:3.7
ADD . ./opt/
WORKDIR /opt/
EXPOSE 5000

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN cmd
RUN ls
RUN ls /opt

CMD ["FLASK_APP=server.py", "flask", "run"]

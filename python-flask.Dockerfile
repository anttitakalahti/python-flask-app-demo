FROM python:3.7
ADD . ./opt/
WORKDIR /opt/

ARG buildtime_variable=default_value
ENV env_var_name=$buildtime_variable

EXPOSE $env_var_name

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV FLASK_APP /opt/server.py

CMD flask run -p $env_var_name

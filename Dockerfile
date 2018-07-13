#FROM python:2.7.15
#FROM casperchiang/cron-python:python2
#FROM pollett/python-cron:2 
FROM ubuntu:14.04

#ENV PYTHONUNBUFFERED 1

#ADD crontab /etc/cron.d/python-cron
#RUN chmod 0644 /etc/cron.d/python-cron
RUN touch /var/log/cron.log

RUN mkdir /code
RUN mkdir -p /files/uploads
WORKDIR /code
COPY . /code/

RUN apt-get update -y
RUN apt-get install python2.7 -y
RUN apt-get install python-pip -y
RUN apt-get install python-dev -y
RUN apt-get install libmysqlclient-dev -y

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN echo "*/5 * * * * python /code/spa_gastos/manage.py process_csv" | crontab -

FROM ubuntu:latest
WORKDIR /srv

RUN apt-get update -y

RUN apt-get install -y python3-pip python3-dev build-essential

COPY . /srv

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

RUN apt-get update -y

CMD flask run --host=0.0.0.0

EXPOSE 5000

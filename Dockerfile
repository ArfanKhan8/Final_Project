FROM ubuntu


ADD . /app
WORKDIR /app
EXPOSE 5000
RUN apt update && apt upgrade
RUN apt-get install -y python3-pip
RUN apt-get install -y openjdk-8-jdk-headless -qq
#RUN apt-get install python3-pip
RUN pip install -r requirements.txt

CMD python3 ./app.py

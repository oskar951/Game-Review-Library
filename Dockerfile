FROM python:3.7

RUN apt-get update && apt-get install -y python3-pip

COPY . .

RUN pip3 install cryptography

RUN pip3 install -r requirements.txt

RUN export 

EXPOSE 5000

ENTRYPOINT ["/usr/local/bin/python3", "app.py"]


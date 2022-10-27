FROM ubuntu:18.04

LABEL Author="Prabin"
LABEL E-mail="prawins2@gmail.com"
LABEL version="0.1"

# Install Required Package 
RUN apt-get update -y 
RUN apt-get install -y python3 python3-dev python3-pip 



# Define Work Directory 

WORKDIR /task

# Copy All files to WorkDir 

COPY ./requirements.txt /task/requirements.txt
COPY ./MyFitness.html /task/MyFitness.html
COPY ./flaskApp.py /task/flaskApp.py
COPY ./functions.py /task/functions.py
COPY ./templates  /task/templates


RUN pip3 install -r requirements.txt

EXPOSE 5000


ENTRYPOINT [ "/usr/bin/python3" ]

CMD [ "flaskApp.py" ]

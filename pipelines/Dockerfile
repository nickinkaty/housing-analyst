FROM ubuntu:20.04

# COPY ENTIRE DIRECTORY
COPY . pipelines/

#PREVEMT PROMPT QUESTION POPPING UP, WHEN INSTALLING DEPENDENCIES
ENV DEBIAN_FRONTEND=noninteractive

# INSTALL DEPENDENCIES
RUN apt-get update
RUN apt-get install -y python3.8 -y openjdk-8-jdk -y python3-pip
RUN pip3 install requests python-decouple python-dotenv pyspark

# INSTALL AIRFLOW
RUN apt-get install libmysqlclient-dev -y libssl-dev -y libkrb5-dev -y
RUN pip3 install apache-airflow==2.1.2
# IF JAVA_HOME ENV NOT SET ERROR => JAVA_HOME is not set
ENV JAVA_HOME  /usr/lib/jvm/java-8-openjdk-amd64/

ENTRYPOINT [ "python3" ]
CMD ["./pipelines/zillow/fetch_real_estates.py"]
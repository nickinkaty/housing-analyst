FROM apache/airflow:2.0.1

# USE ROOT TO DOWNLOAD DEPENDENCIES
USER root

#PREVEMT PROMPT QUESTION POPPING UP, WHEN INSTALLING DEPENDENCIES
ENV DEBIAN_FRONTEND=noninteractive

# INSTALL DEPENDENCIES
# Install software source manager
RUN apt-get update
RUN apt-get -y install software-properties-common
# Add mirror with openjdk-8-jdk
RUN apt-add-repository 'deb http://security.debian.org/debian-security stretch/updates main'
RUN apt-get update
# -------------------------------------------------------------------------------------------------
RUN apt-get install -y openjdk-8-jdk -y python3-pip -y vim
RUN pip3 install requests python-decouple python-dotenv pyspark

# IF JAVA_HOME ENV NOT SET ERROR => JAVA_HOME is not set
ENV JAVA_HOME  /usr/lib/jvm/java-8-openjdk-amd64/

# SWITCH BACK TO AIRFLOW
USER airflow

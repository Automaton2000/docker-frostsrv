FROM alpine:3.9

# update and install dependencies
RUN apk --update add --virtual frostsrv-dependencies build-base gcc openjdk8 python3-dev libxml2-dev libxslt-dev py3-pip && pip3 install lxml

# get and install tomcat
RUN mkdir /usr/local/tomcat
RUN wget http://www-us.apache.org/dist/tomcat/tomcat-8/v8.5.37/bin/apache-tomcat-8.5.37.tar.gz -O /tmp/tomcat.tar.gz
RUN cd /tmp && tar xvfz tomcat.tar.gz
RUN cp -Rv /tmp/apache-tomcat-8.5.37/* /usr/local/tomcat/

# copy settings xml file and a script to modify it
COPY FROST-Server.xml ./
COPY mod_frostsrv_xml.py ./

# get the precompiled FROST-Server war file
RUN wget -O FROST-Server.war https://bintray.com/fraunhoferiosb/Maven/download_file?file_path=de%2Ffraunhofer%2Fiosb%2Filt%2FFROST-Server%2FFROST-Server.MQTTP%2F1.9%2FFROST-Server.MQTTP-1.9.war

# download postgres and postgis plugin
RUN wget https://repo.maven.apache.org/maven2/org/postgresql/postgresql/9.4.1212/postgresql-9.4.1212.jar
RUN wget https://repo.maven.apache.org/maven2/net/postgis/postgis-jdbc/2.2.1/postgis-jdbc-2.2.1.jar

EXPOSE 8080

# move everything in place, alter settings xml and start tomcat
CMD mv FROST-Server.war /usr/local/tomcat/webapps/ && \
    mv postgresql-9.4.1212.jar /usr/local/tomcat/lib/ && \
    mv postgis-jdbc-2.2.1.jar /usr/local/tomcat/lib/ && \
    python3 mod_frostsrv_xml.py && \
    mkdir /usr/local/tomcat/conf/Catalina && \
    mkdir /usr/local/tomcat/conf/Catalina/localhost && \
    mv FROST-Server.xml /usr/local/tomcat/conf/Catalina/localhost && \
    /usr/local/tomcat/bin/catalina.sh run


FROM openjdk:8u212

COPY dreamer-cms.jar /

RUN mkdir /dreamer-cms 

CMD [ "java", "-jar", "/dreamer-cms.jar" ]

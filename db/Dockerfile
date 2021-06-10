FROM mysql:5.6

ENV MYSQL_DATABASE control_asistencia 
ENV MYSQL_ROOT_PASSWORD pass
COPY control_asistencia.sql /docker-entrypoint-initdb.d/control_asistencia.sql

EXPOSE 3306
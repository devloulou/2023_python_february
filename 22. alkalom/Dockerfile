# ő a base image: mindig kell legalább 1 base image
FROM postgres

ENV POSTGRES_PASSWORD postgres
ENV POSTGRES_DB postgres
ENV POSTGRES_USER postgres

COPY world.sql /docker-entrypoint-initdb.d/
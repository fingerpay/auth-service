FROM postgres:9.6.23
USER root
MAINTAINER ITO Manaki <colk@fingerpay.app>

ENV LC_ALL=en_US.UTF-8 \
    TZ=JST-9 \
    TERM=xtermdocker-attachingdocker-attaching

# TODO: Postgeres が update のリストに入っていなくて Not Found で確定でコケるので update できない
# RUN apt-get update \
#     激重なので upgrade はしない
#     && apt-get upgrade -y \
#     && apt-get install -y --no-install-recommends locales

# RUN localedef -f UTF-8 -i en_US en_US.UTF-8

# 激重なので cleanup はしない
# RUN apt-get autoremove -y \
#    && apt-get clean -y \
#    && rm -rf /var/lib/apt/lists/*

COPY ./docker/postgres/initdb /docker-entrypoint-initdb.d

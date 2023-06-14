FROM jupyter/datascience-notebook as builder

USER root

RUN apt-get update \
  && apt-get install --fix-missing -y inkscape \
  && rm -rf /var/lib/apt/lists/*

USER ${NB_UID}

RUN pip install qrcode
USER root

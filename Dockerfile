FROM jupyter/datascience-notebook as builder

USER root

RUN apt update \
  && apt install -y inkscape \
  && rm -rf /var/lib/apt/lists/*

USER ${NB_UID}

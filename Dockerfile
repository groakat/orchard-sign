FROM jupyter/datascience-notebook:2023-06-13 as builder

USER root

# install inkscape
RUN apt-get update \
  && apt-get install --fix-missing -y inkscape \
  && rm -rf /var/lib/apt/lists/*

# install montserrat font
RUN curl -L -o montserrat.tar.gz https://github.com/JulietaUla/Montserrat/archive/refs/tags/v7.222.tar.gz \
  && mkdir montserrat \
  && tar -xvf montserrat.tar.gz -C montserrat --strip-components=1 \
  && /usr/share/fonts/truetype/montserrat \
  && mkdir /usr/share/fonts/truetype/montserrat/ \
  && cp montserrat/fonts/ttf/* /usr/share/fonts/truetype/montserrat/ \
  && rm -r montserrat*

USER ${NB_UID}

RUN pip install qrcode
USER root

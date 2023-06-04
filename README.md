# Orchard Sign Generator

## High-level Plan

- [x] ingest template SVG
- [ ] read plant database
- [ ] for each entry: 
    - [ ] replace placeholders with plan data (e.g. name, location number, etc)
    - [ ] save modified SVG file
- [ ] for each saved SVG file, feed through Inkscape to vecorize fonts, save again

## How to use
This repository contains a `Dockerfile` that will contain all software requirements of this project. To start off easy, the base image is the juptyter-datascience image that contains all tooling than we need (and a lot more). 

You can build and startup this image via the `start.sh` script. Once it is done building the docker image, open the link it prints out. It will look something like this:

```bash
http://127.0.0.1:8888/lab?token=6432d5e7d895a1f87eee2d6cbb36918af8cef498cf889317
```

(the token changes, so you need to open the link that is generated for you)
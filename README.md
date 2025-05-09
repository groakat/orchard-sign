# Orchard Sign Generator

## High-level Plan

- [x] ingest template SVG
- [ ] read plant database
- [ ] for each entry: 
    - [ ] replace placeholders with plan data (e.g. name, location number, etc)
    - [ ] save modified SVG file
- [ ] for each saved SVG file, feed through Inkscape to vecorize fonts, save again

## How to use
### With Docker
This repository contains a `Dockerfile` that will contain all software requirements of this project. To start off easy, the base image is the juptyter-datascience image that contains all tooling than we need (and a lot more). 

First, make sure you have Docker installed (see: https://www.docker.com/).

You can build and startup this image via the `start.sh` script. Once it is done building the docker image, open the link it prints out. It will look something like this:

```bash
http://127.0.0.1:8888/lab?token=6432d5e7d895a1f87eee2d6cbb36918af8cef498cf889317
```

(the token changes, so you need to open the link that is generated for you)

You will see the Jupyter environment starting up, showing a single folder on the left, called `work`. This folder will be linked to this repo, which contains the `notebook` folder. Please use this `notebook` folder to save any ipython notebooks / playgrounds.

### With nix
(only tested with nix darwin (i.e. nix on macOS), see note about inkscape below)

After you have nix installed (I used the [graphical installer from Determinate Systems](https://determinate.systems/posts/graphical-nix-installer/)), run: 

- `nix develop` 

and after the build is complete, the jupyter server will open.

#### Note about Inkscape on macOS
Inkscape on nix is currently [broken](https://github.com/NixOS/nixpkgs/issues/383860) on macOS, so please install it separately from here https://inkscape.org/release.

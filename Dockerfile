# Docker file for lungct ChRIS plugin app
#
# Build with
#
#   docker build -t <name> .
#
# For example if building a local version, you could do:
#
#   docker build --build-arg UID=$UID -t local/pl-lungCT .
#
# In the case of a proxy (located at 192.168.13.14:3128), do:
#
#    export PROXY=http://192.168.13.14:3128
#    docker build --build-arg http_proxy=$PROXY --build-arg UID=$UID -t local/pl-lungCT .
#
# To run an interactive shell inside this container, do:
#
#   docker run -ti --entrypoint /bin/bash local/pl-lungct
#
# To pass an env var HOST_IP to container, do:
#
#   docker run -ti -e HOST_IP=$(ip route | grep -v docker | awk '{if(NF==11) print $9}') --entrypoint /bin/bash local/pl-lungCT
#
# To debug from within a container:
#
#   docker run -ti -v $(pwd)/lungct:/usr/local/lib/python3.8/dist-packages/lungct -v $(pwd)/out:/outgoing local/pl-lungct lungct /outgoing
#

FROM fnndsc/ubuntu-python3:latest
LABEL MAINTAINER="dev@babymri.org"

# Pass a UID on build command line (see above) to set internal UID
ARG UID=1001
ENV UID=$UID DEBIAN_FRONTEND=noninteractive

WORKDIR /usr/local/src
COPY . .
RUN pip --disable-pip-version-check install .                   \
    && useradd -u $UID -ms /bin/bash localuser                  \
    && apt-get install -y sudo

RUN echo "localuser:localuser" | chpasswd                       \
    && addgroup localuser sudo                                  \
    && echo "localuser ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Start as user localuser
# USER localuser

WORKDIR /usr/local/bin
CMD ["lungct", "--help"]

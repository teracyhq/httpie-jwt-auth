FROM python:2.7

LABEL authors="hoatle <hoatle@teracy.com>"

RUN mkdir -p /opt/app/

ENV TERM=xterm APP=/opt/app

# add more arguments from CI to the image so that `$ env` should reveal more info
ARG CI_BUILD_ID
ARG CI_BUILD_REF
ARG CI_REGISTRY_IMAGE
ARG CI_PROJECT_NAME
ARG CI_BUILD_REF_NAME
ARG CI_BUILD_TIME
ARG CI_BUILD_NUMBER
ARG CI_BUILDER

# required when build
ARG HTTPie_VERSION

ENV CI_BUILD_ID=$CI_BUILD_ID CI_BUILD_REF=$CI_BUILD_REF CI_REGISTRY_IMAGE=$CI_REGISTRY_IMAGE \
    CI_PROJECT_NAME=$CI_PROJECT_NAME CI_BUILD_REF_NAME=$CI_BUILD_REF_NAME CI_BUILD_TIME=$CI_BUILD_TIME \
    CI_BUILD_NUMBER=$CI_BUILD_NUMBER CI_BUILDER=$CI_BUILDER \
    HTTPie_VERSION=$HTTPie_VERSION

WORKDIR $APP

ADD requirements-dev.txt $APP/requirements-dev.txt

RUN pip install -r $APP/requirements-dev.txt

RUN pip install httpie==$HTTPie_VERSION

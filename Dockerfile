# base: start with Alpine, install postgres dependencies
FROM python:3.7.3-alpine AS base
RUN apk update && apk add bash build-base postgresql-dev libffi-dev

ENV INSTALL_PATH /code
RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH

# libs: install dependencies
FROM base AS libs
COPY MANIFEST.in README.md requirements.txt setup.cfg setup.py $INSTALL_PATH/
RUN pip install -r requirements.txt .[deploy]

COPY entrypoint.sh $INSTALL_PATH/
ENTRYPOINT ["/code/entrypoint.sh"]
CMD ["server"]

# code: copy in the code
FROM libs AS code
ARG BUILD_NUM
ARG SHA1
ENV BACKEND__BUILD_INFO__BUILD_NUM ${BUILD_NUM}
ENV BACKEND__BUILD_INFO__SHA1 ${SHA1}
COPY backend backend


# test: install test dependencies
FROM code AS test
RUN pip install -r requirements.txt .[lint,test,typehinting]

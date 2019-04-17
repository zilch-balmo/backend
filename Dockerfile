FROM python:3.7.3-alpine

RUN apk update && apk add bash build-base postgresql-dev libffi-dev

ENV INSTALL_PATH /code
RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH

COPY MANIFEST.in README.md entrypoint.sh requirements.txt setup.cfg setup.py .
RUN pip install -r requirements.txt .[deploy,lint,test,typehinting]
COPY backend backend

ENTRYPOINT ["/code/entrypoint.sh"]
CMD ["server"]

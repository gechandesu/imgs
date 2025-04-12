FROM alpine:latest
RUN apk update && apk add python3 py3-bottle py3-gunicorn
ADD . /opt/imgs
RUN mkdir -p /opt/imgs/uploads
WORKDIR /opt/imgs
EXPOSE 5000
CMD gunicorn imgs:app --bind :5000

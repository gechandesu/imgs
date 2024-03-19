FROM alpine:latest
MAINTAINER "Bayesia-SAS'
RUN apk update && apk add python3 py3-pip --no-cache
RUN pip install gunicorn --no-cache-dir --break-system-packages
ADD app/ /opt/imgs
RUN mkdir -p /opt/imgs/uploads
WORKDIR /opt/imgs
RUN pip install --requirement requirements.txt --no-cache-dir --break-system-packages
EXPOSE 5000
CMD gunicorn imgs:app --bind :5000

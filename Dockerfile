FROM python:latest
ADD . /opt/imgs
RUN mkdir -p /opt/imgs/uploads
WORKDIR /opt/imgs
RUN pip install --upgrade pip && pip install --requirement requirements.txt
EXPOSE 5000
CMD gunicorn imgs:app --bind :5000

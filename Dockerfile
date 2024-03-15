FROM python:3.9-alpine
RUN pip install --upgrade pip --no-cache-dir && pip install gunicorn --no-cache-dir
ADD app/ /opt/imgs
RUN mkdir -p /opt/imgs/uploads
WORKDIR /opt/imgs
RUN pip install --requirement requirements.txt --no-cache-dir
EXPOSE 5000
CMD gunicorn imgs:app --bind :5000

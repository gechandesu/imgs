FROM python:3.9-alpine
ADD app/ /opt/imgs
RUN mkdir -p /opt/imgs/uploads
WORKDIR /opt/imgs
RUN pip install --upgrade pip && pip install --requirement requirements.txt
RUN pip install gunicorn
EXPOSE 5000
CMD gunicorn imgs:app --bind :5000

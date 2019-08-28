FROM python:3.7-alpine
ADD apk gcc
WORKDIR /opt/exApi
COPY requirements.txt ./

RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple

COPY . .

CMD ["gunicorn","start:app","./gunicorn.conf.py"]
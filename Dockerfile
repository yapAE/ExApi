FROM alpine
RUN apk update \
    && apk upgrade \
    && apk add \
    build-base \
    python3 \
    python3-dev

ENV TIMEZONE   Asia/Shanghai

WORKDIR /opt/exApi
COPY requirements.txt ./

RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple

COPY . .

EXPOSE 8080

CMD ["gunicorn","start:app","./gunicorn.conf.py"]
FROM alpine
RUN apk update \
    && apk upgrade \
    && apk add \
    build-base \
    python3 \
    python3-dev \
    python3-pip

ENV TIMEZONE   Asia/Shanghai
RUN echo "${TIMEZONE}" > /etc/timezone
WORKDIR /opt/exApi
COPY requirements.txt ./
RUN pip3 install --upgrade pip setuptools
RUN pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple

COPY . .

EXPOSE 8080

CMD ["gunicorn","start:app","./gunicorn.conf.py"]
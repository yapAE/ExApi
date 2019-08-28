FROM alpine
RUN apk update \
    && apk upgrade \
    && apk add --no-cache\
    build-base \
    python3 \
    python3-dev \
    libffi-devel \
    openssl-devel \
    && python3 -m ensurepip
ENV TIMEZONE   Asia/Shanghai
RUN echo "${TIMEZONE}" > /etc/timezone \
    && ln -sf /usr/share/zoneinfo/${TIME_ZONE} /etc/localtime 
WORKDIR /opt/exApi
COPY requirements.txt ./
RUN pip3 install --upgrade pip setuptools
RUN pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple

COPY . .

EXPOSE 8080

CMD ["gunicorn","start:app","./gunicorn.conf.py"]
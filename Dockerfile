FROM python:3.8-alpine
EXPOSE 8000

RUN apk add \
    wget \
    gcc \
    make \
    zlib-dev \
    libffi-dev \
    openssl-dev \
    musl-dev


WORKDIR /opt/smart_home
COPY smart_home/ /opt/smart_home
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]

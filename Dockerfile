FROM python

WORKDIR /app

COPY requirements/dev.txt /app/requirements.txt

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

RUN pip install -r /app/dev.txt \
    && rm -rf /root/.cache/pip

COPY . /app

EXPOSE 9000

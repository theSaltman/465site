FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

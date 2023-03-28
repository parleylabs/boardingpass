FROM python:3.9.6

ENV PYTHONUNBUFFERED=1

WORKDIR /backend

# copy from the current directory of the Dockerfile to /api in the image
COPY . .

RUN pip install --upgrade pip setuptools
RUN pip install -r requirements.txt



EXPOSE 8000

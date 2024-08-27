FROM ubuntu:22.04

LABEL authors="fwy"

RUN mkdir /fwy
WORKDIR /fwy

RUN apt update
RUN apt install ffmpeg python3-pip -y

ADD requirements.txt /fwy

RUN python3 -m pip install -r /fwy/requirements.txt

ADD main.py /fwy
ADD index.html /fwy

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0"]

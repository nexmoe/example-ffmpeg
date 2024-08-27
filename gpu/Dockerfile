FROM linuxserver/ffmpeg

LABEL authors="fwy"

RUN mkdir /fwy
WORKDIR /fwy

RUN apt update
RUN apt install python3-pip python3-venv -y

ADD requirements.txt /fwy

RUN python3 -m venv /fwy/venv
RUN /fwy/venv/bin/python -m pip install -r /fwy/requirements.txt

ADD main.py /fwy
ADD index.html /fwy

ENTRYPOINT ["/fwy/venv/bin/uvicorn", "main:app", "--host", "0.0.0.0"]

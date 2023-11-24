FROM python:3.9

RUN mkdir /auto_caption_system

WORKDIR /auto_caption_system

COPY requirements.txt .
COPY src ./src
RUN pip install -r requirements.txt
CMD python src/main.py
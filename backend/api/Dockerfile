FROM python:3.9.5

RUN mkdir /auto_caption_system

WORKDIR /auto_caption_system

RUN apt-get -y update
RUN apt-get install -y --fix-missing \
    build-essential \
    cmake \
    gfortran \
    git \
    wget \
    curl \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libatlas-base-dev \
    libavcodec-dev \
    libavformat-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    python3-dev \
    python3-numpy \
    software-properties-common \
    zip \
    && apt-get clean && rm -rf /tmp/* /var/tmp/*

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN cd ~ && \
    git clone https://github.com/ageitgey/face_recognition && \
    cd  face_recognition/ && \
    python setup.py install

RUN cd ..
COPY megrations ./megrations
COPY docker ./docker
COPY src ./src
COPY alembic.ini .
RUN rm -rf face_recognition
RUN chmod a+x docker/*.sh

#CMD python src/main.py

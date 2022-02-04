FROM ramadhani892/ramutod:slim-buster

RUN git clone -b KY-UBOT https://github.com/rizkypratama2/KY-UBOT /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/rizkypratama2/KY-UBOT/KY-UBOT/requirements.txt

CMD ["python3","-m","userbot"]

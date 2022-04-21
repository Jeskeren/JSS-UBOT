FROM ramadhani892/ramagans:slim-buster

RUN git clone -b JS-UBOT https://github.com/Jeskeren/JSS-UBOT /root/userbot
WORKDIR /root/userbot

CMD ["python3", "-m", "userbot"]

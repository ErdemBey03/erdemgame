

WORKDIR /app

COPY requiremets.txt /app/

RUN pip3 install -r requirements.txt

COPY . /app

CMD node bot.js

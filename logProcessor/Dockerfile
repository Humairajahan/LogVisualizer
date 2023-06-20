FROM python:3.10-slim-buster 

WORKDIR /app

COPY . /app/.

RUN chmod +x bash_scripts/DataGenerator.sh
RUN chmod +x bash_scripts/logParser.sh
RUN chmod +x bash_scripts/merge.sh

CMD ["./bash_scripts/merge.sh"]
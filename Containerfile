#questo comando serve per indicare quale linguaggio utilizzare
FROM python:3


#questi comandi servono per aggiungere i file al Container
COPY data.yml
COPY app.yml
COPY main.py


#questo comando serve per installare tutte le librerie contenute nel file Requirements
RUN pip install -r "Requirements.txt"


#questo comando serve per eseguire il file main.py
CMD [ "python", "main.py" ]




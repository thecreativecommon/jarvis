FROM python:3 
ADD requirements.txt / 
RUN pip install -r requirements.txt 
ADD main.py /
ADD .env /
CMD [ "python", "./main.py" ]

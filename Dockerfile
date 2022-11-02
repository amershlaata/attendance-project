FROM python:3.8.3-slim
COPY . /app 
#copy all the files to dir /app
WORKDIR /app 
#go to /app
RUN pip install -r requirements.txt
 #install all the packegs from reqirements
EXPOSE 5000 
#port 5000
CMD ["python3","flask2.py"] 
# command that run the project
#flask2.py this file for runing the flask application



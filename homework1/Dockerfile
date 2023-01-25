FROM python:3.9
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD ["python", "./backend/app.py"]

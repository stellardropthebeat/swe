FROM python:3.9

# Create a new user
RUN adduser --disabled-password --gecos '' app_user

COPY ../../.. /app

WORKDIR /app

RUN pip install --upgrade pip

RUN pip3 install -r requirements.txt

EXPOSE 5000

# Switch to the newly created user
USER app_user

CMD ["python", "./app.py"]

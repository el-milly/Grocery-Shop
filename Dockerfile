FROM python:3.13.3-alpine
WORKDIR /project
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
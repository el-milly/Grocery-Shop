FROM python:3.12-slim

WORKDIR /order

COPY requirements.txt .
RUN pip install --no-cache -r requirements.txt \
 --index-url https://pypi.tuna.tsinghua.edu.cn/simple \
 --trusted-host pypi.tuna.tsinghua.edu.cn
COPY . .
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
FROM python:3
COPY . /app
RUN pip install --upgrade pip && pip install psycopg2
WORKDIR /app
CMD python3 main.py
FROM python:3.10-bullseye

RUN pip install openpyxl flask flask_cors
COPY . /

EXPOSE 5000

CMD ["python3", "/bible-api.py"]

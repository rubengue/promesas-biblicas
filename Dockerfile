FROM python:3.10-bullseye

COPY . /
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python3", "/bible-api.py"]

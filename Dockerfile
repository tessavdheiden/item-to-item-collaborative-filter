FROM python:3.8-slim-buster

WORKDIR /app

COPY ./requirements.txt /app/
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt


COPY ./final_model.joblib /app/
COPY ./main.py /app/


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
FROM python:latest

COPY requirements.txt /
RUN pip install --no-cache-dir --upgrade -r requirements.txt


COPY final_model.joblib /
COPY main.py /


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
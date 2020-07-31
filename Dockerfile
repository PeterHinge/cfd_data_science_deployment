FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

ENV DEFAULT_MODEL_PATH=/app/models/prediction.joblib
ENV API_KEY=sample_api_key
ENV APP_MODULE="src.app.main:app"
ENV PYTHONPATH=/app

COPY . /app

WORKDIR /app

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install .
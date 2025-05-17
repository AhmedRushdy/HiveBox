FROM python:alpine

WORKDIR /app
ENV APP_VERSION="v.1.0.0"
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "app.py"]
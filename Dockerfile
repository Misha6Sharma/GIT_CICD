FROM python:3.10-slim

WORKDIR /app

# Copy requirements first
COPY app/requirements.txt /app/requirements.txt

# Install dependencies
RUN python -m pip install --upgrade pip && \
    pip install -r /app/requirements.txt

# Copy code
COPY . /app

# Run FastAPI server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

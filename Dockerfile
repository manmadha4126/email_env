FROM python:3.10.13-slim-bullseye

WORKDIR /app

# Avoid buffering issues
ENV PYTHONUNBUFFERED=1

# Copy only requirements first (better caching)
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy rest of the code
COPY . .

EXPOSE 7860

CMD ["python", "-m", "server.app"]
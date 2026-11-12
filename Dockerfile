FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements-deploy.txt setup.py README.md ./
COPY src ./src
COPY app.py ./
COPY templates ./templates
COPY model ./model

RUN pip install --no-cache-dir -r requirements-deploy.txt

ENV PORT=7860
EXPOSE 7860

CMD ["python", "app.py"]

FROM python:3.10-slim

WORKDIR /app

ADD . /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    libblas-dev \
    liblapack-dev \
    gfortran \
    g++ \  
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN --mount=type=secret,id=CODEARTIFACT_AUTH_TOKEN \
    pip install --upgrade pip && \
    CODEARTIFACT_AUTH_TOKEN="$(cat /run/secrets/CODEARTIFACT_AUTH_TOKEN)" pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]
FROM python:3.7

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

RUN apt-get update && apt-get install -y \
    build-essential \
    openjdk-11-jre-headless \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY . .

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "--theme.base=dark"]

CMD ["app.py"]

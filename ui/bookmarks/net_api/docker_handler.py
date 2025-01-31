"""
docker_handler.py
Keyword: net_api_docker

Pliki Dockerfile, docker-compose do uruchamiania kontenerów z aplikacją i bazą.
W praktyce - generowanie Dockerfile / docker-compose.
"""

DOCKERFILE_TEMPLATE = """
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "-m", "src.main"]
"""

def create_dockerfile(output_path="Dockerfile"):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(DOCKERFILE_TEMPLATE)
    print(f"Utworzono Dockerfile w {output_path}")

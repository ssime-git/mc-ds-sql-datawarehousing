FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /app

COPY pyproject.toml uv.lock ./
COPY src ./src

RUN uv sync --package app --no-dev

EXPOSE 8501

CMD ["uv", "run", "--package", "app", \
     "streamlit", "run", "src/app/app/main.py", \
     "--server.address", "0.0.0.0", "--server.port", "8501"]

FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /app

COPY pyproject.toml uv.lock ./
COPY src ./src

RUN uv sync --package api --no-dev

CMD ["uv", "run", "--package", "api", \
     "uvicorn", "api.main:app", \
     "--host", "0.0.0.0", "--port", "8000"]

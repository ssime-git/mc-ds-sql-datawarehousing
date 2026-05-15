.PHONY: install etl up down test slides reset

install:
	uv sync

etl:
	uv run --package etl python -m etl.main

up:
	docker compose up -d

down:
	docker compose down

test:
	uv run pytest tests/ -v

slides:
	npx @marp-team/marp-cli slides/data-engineering-sql.md \
		--html --allow-local-files \
		-o slides/out/index.html

reset:
	docker compose down --volumes --remove-orphans 2>/dev/null || true
	rm -f db/census.db
	rm -rf data/
	rm -rf .venv/
	@echo "Reset complet — relancer avec: make install && make etl && make up"

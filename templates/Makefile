.PHONY: install lint format test

install:
	uv sync --dev

lint:
	ruff check .
	mypy src

format:
	ruff format .

test:
	pytest -q

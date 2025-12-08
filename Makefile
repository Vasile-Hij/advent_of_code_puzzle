.ONESHELL:
SHELL := /bin/zsh

UV_BIN ?= uv

.PHONY: init install-uv setup up down help lock

help:
	@cat Makefile

install-uv:
	@command -v $(UV_BIN) >/dev/null 2>&1 || \
	curl -LsSf https://astral.sh/uv/install.sh | sh
	@echo "uv installed or already present"

setup: install-uv
	@test -f pyproject.toml || $(UV_BIN) init --bare
	@echo "created pyproject.toml"
	$(UV_BIN) add --dev ruff pre-commit black pydantic termcolor ipdb
	$(UV_BIN) sync
	@touch .pre-commit-config.yaml'
	@echo "Need to add info to '.pre-commit-config.yaml' file."
	@PATH="$$HOME/.local/bin:$$PATH" $(UV_BIN) run pre-commit install
	@echo "pre-commit installed"

up: 
	$(UV_BIN) sync
	@test -d .venv || $(UV_BIN) sync
	@source .venv/bin/activate && cd src && exec $$SHELL -l

down:
	@deactivate 2>/dev/null || true

lock:
	$(UV_BIN) lock
	@echo "Created/updated uv.lock"

init: setup lock up

pyright:
	uv run pyright

set shell := ["bash", "-c"]

uv_bin := env("UV_BIN", "uv")

# Show all commands
help:
    @just --list

# Install uv package manager
install-uv:
    @command -v {{uv_bin}} >/dev/null 2>&1 || curl -LsSf https://astral.sh/uv/install.sh | sh
    @echo "uv installed or already present"

# Initialize project
setup: install-uv
    @test -f pyproject.toml || {{uv_bin}} init --bare
    @echo "created pyproject.toml"
    {{uv_bin}} add --dev ruff pre-commit black pydantic termcolor ipdb pytest pytest-cov pyright
    {{uv_bin}} sync
    @touch .pre-commit-config.yaml
    @echo "Need to add info to '.pre-commit-config.yaml' file."
    @PATH="$HOME/.local/bin:$PATH" {{uv_bin}} run pre-commit install
    @echo "pre-commit installed"

# Activate virtual environment
up:
    {{uv_bin}} sync
    @test -d .venv || {{uv_bin}} sync
    {{uv_bin}} pip install -e .
    @source .venv/bin/activate && cd src && exec $SHELL -l

# Deactivate virtual environment
down:
    @deactivate 2>/dev/null || true

# Update dependencies
lock:
    {{uv_bin}} lock
    @echo "Created/updated uv.lock"

# Full initialization
init: setup lock up

# Highlights semantic and stylistic issue
lint:
    {{uv_bin}} run ruff check . --fix
    {{uv_bin}} run ruff format .
    {{uv_bin}} run pyright .

# Run the test suite
test:
    {{uv_bin}} run pytest tests/ -v

# Run lint + test at once
check: lint test

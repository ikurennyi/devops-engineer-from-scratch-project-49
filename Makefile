install:
	uv sync

brain-games:
	uv run brain-games

brain-even:
	uv run brain-even

build:
	uv build

test:
	uv run pytest

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check brain_games

.PHONY: test

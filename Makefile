it: test

test: build test-static test-code

test-static: test-lint test-type

test-code:
	poetry run pytest -c pyproject.toml --mypy-ini-file=pyproject.toml --count=20 --no-cov-on-fail --cov-report= --cov

test-lint:
	poetry run black --check .
	poetry run flake8 --ignore E501

test-type:
	poetry run mypy --config-file pyproject.toml .

build:
	poetry install

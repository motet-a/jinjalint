.PHONY: lint
lint:
	poetry run pycodestyle jinjalint

.PHONY: test
test:
	poetry run python -m jinjalint.test

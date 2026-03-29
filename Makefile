.PHONY: test

test:
	poetry run python -m unittest discover -s tests -q

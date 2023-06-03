install:
	pip install -r requirements.txt

lint:
	pylint multiply.py

test:
	python -m pytest -vv test_multiply.py
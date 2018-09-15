setup:
	pip install pipenv
	pipenv install --dev --three

test:
	pipenv run -- pylint parquet_metadata
	pipenv run -- pytest --cov=parquet_metadata
	pipenv run -- codecov

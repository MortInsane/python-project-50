install:
	poetry install

package-build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
# ---- Setup project
install:
	poetry install

# ---- Database
migrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

check-migrations:
	poetry run python manage.py migrate --fake

flush:
	poetry run python manage.py flush

load-fixtures:
	poetry run python manage.py loaddata task_manager/fixtures/labels.yaml; \
	poetry run python manage.py loaddata task_manager/fixtures/statuses.yaml

superuser:
	poetry run python manage.py createsuperuser

load-demo-data:
	poetry run python manage.py loaddata task_manager/tests/fixtures/*.yaml

# ---- Linter, Tests
lint:
	poetry run flake8 --config linter-setup.cfg

test:
	poetry run pytest

coverage:
	poetry run pytest --cov=task_manager --cov-report=xml

# ---- Django shell
django-shell:
	poetry run python manage.py shell

# ---- Run
run:
	poetry run python manage.py runserver
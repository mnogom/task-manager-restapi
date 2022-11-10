#!/bin/sh

if [ "$DATABASE_CORE" = "postgres" ]
then
  echo "Waiting for postgres"

  while ! nc -z "$SQL_HOST" "$SQL_PORT" ; do
      sleep 0.1
  done
fi

#poetry run python manage.py collectstatic --no-input
# poetry run python manage.py flush --no-input
poetry run python manage.py migrate

exec "$@"

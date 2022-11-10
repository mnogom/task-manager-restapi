# pull official base image
FROM python:3

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project
COPY . .

# install dependecies
RUN pip3 install --upgrade pip
RUN pip3 install poetry
RUN poetry config virtualenvs.in-project true --local
COPY poetry.lock pyproject.toml ./
RUN poetry install

# run entrypoint.sh
ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]
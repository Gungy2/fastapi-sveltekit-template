FROM python:3.9

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY pyproject.toml .
RUN poetry install --no-dev

COPY /backend /backend

CMD ["poetry", "run", "start"]
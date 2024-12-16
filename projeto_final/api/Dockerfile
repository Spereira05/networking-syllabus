FROM python:3.9-slim

# Install poetry
RUN pip install --no-cache-dir poetry

WORKDIR /app

COPY pyproject.toml poetry.lock /app/
RUN poetry install --no-root --no-dev

COPY src/ /app/src/

EXPOSE 5000
CMD ["poetry", "run", "python", "src/app.py"]

# Use an official Python runtime as a parent image
FROM python:3.12.3-slim

ENV PYTHONUNBUFFERED 1
# Set the working directory in the container to /app
WORKDIR /app

# Install Poetry
RUN pip install poetry

COPY pyproject.toml poetry.lock ./

# Install project dependencies
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi --no-root

  
COPY . .
RUN chmod +x /app/docker-entrypoint.sh

# Make port 50051 available to the world outside this container
EXPOSE 50051

# Run server.py when the container launches
ENTRYPOINT ["/app/docker-entrypoint.sh"]
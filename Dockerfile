# Use an official Python runtime as a parent image
FROM python:3.12.3-slim

ENV PYTHONUNBUFFERED 1
# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install Poetry
RUN pip install poetry

# Install project dependencies
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi --no-root

# Make port 50051 available to the world outside this container
EXPOSE 50051

# Run server.py when the container launches
CMD ["scripts/docker-entrypoint.sh"]

# Use the official Python 3.12 Alpine image
FROM python:3.12-alpine

# Set environment variables to prevent Python from buffering output and creating .pyc files
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Install required system packages
RUN apk add --no-cache \
    netcat-openbsd \
    gettext \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev \
    bash \
    python3-dev \
    mariadb-dev

# Create and set the working directory
RUN mkdir /code
WORKDIR /code

# Copy project files into the container
COPY . /code/
# Upgrade pip and install project dependenciespython
RUN set -e; \
    python -m pip install --upgrade pip;\
    pip install -r /code/utils/requirements.txt;\
    chmod +x /code/docker/entrypoints/entrypoint.sh;

# Expose the port the app will use
EXPOSE 8000

# Specify the entrypoint script to run when the container starts
ENTRYPOINT ["sh", "/code/docker/entrypoints/entrypoint.sh"]

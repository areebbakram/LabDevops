# # Dockerfile
# FROM python:3.10-slim

# # Prevent Python from writing pyc files and buffering output
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# # Set working directory
# WORKDIR /app

# # Copy and install dependencies
# COPY requirements.txt /app/
# RUN pip install --upgrade pip && pip install -r requirements.txt

# # Copy the project code into the container
# COPY . /app/

# # Default command (can be overridden by docker-compose)
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBUG=1
ENV DJANGO_ALLOWED_HOSTS="*"
ENV CI=true

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# Skip migrate if DB missing, but container MUST start
CMD sh -c "python manage.py migrate || echo 'Skipping migrate' && python manage.py runserver 0.0.0.0:8000"

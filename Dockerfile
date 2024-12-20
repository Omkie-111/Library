# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt into the container
COPY requirements.txt .

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files into the container
COPY . .

# Expose port 8000 for Django to run on
EXPOSE 8000

# Set the environment variable for Django
ENV DJANGO_SETTINGS_MODULE=library_management.settings

# Run the Django app (replace with `gunicorn` for production)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# 1. Use a slim Python image to keep the size small
FROM python:3.11-slim

# 2. Set environment variables
# Prevents Python from writing .pyc files and ensures output is logged immediately
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Set the working directory inside the container
WORKDIR /app

# 4. Install system dependencies
# Some Python packages (like psycopg2 for Postgres) need build tools
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 5. Install Python dependencies
# We copy this first so Docker can cache the "layer" and not re-install every time you change your code
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy the rest of your application code
COPY . .

# 7. Expose the port FastAPI runs on
EXPOSE 8000

# 8. Start the FastAPI server using Uvicorn
# --host 0.0.0.0 is MANDATORY inside Docker to allow external access
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
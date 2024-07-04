#!/bin/sh

# Function to check database connection
check_database_connection() {
    echo "Checking database connection..."
    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
        sleep 1
    done
    echo "Database is ready."
}

# Function to check Redis connection
check_redis_connection() {
    echo "Checking Redis connection..."
    while ! nc -z $REDIS_HOST $REDIS_PORT; do
        sleep 1
    done
    echo "Redis is ready."
}

# Wait for the database to be ready before running Django
check_database_connection

# Check Redis connection
check_redis_connection

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Collect static files (if needed)
# Uncomment the line below if you want to collect static files during container startup
# python manage.py collectstatic --noinput

# Check the environment variable to determine the mode (development or production)
if [ "$DJANGO_ENV" = "production" ]; then
    echo "Starting Daphne in production mode..."
    daphne -p 8000 -b 0.0.0.0 inside.asgi:application
else
    echo "Starting Django development server..."
    python manage.py runserver 0.0.0.0:8000
fi
# Use a lightweight Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy your app into the container
COPY app.py .

# Expose the port your app listens on
EXPOSE 8080

# Run the app
CMD ["python", "app.py"]

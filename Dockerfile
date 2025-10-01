# Use lightweight Python base image
FROM python:3.11-slim

WORKDIR /app
COPY app.py .

EXPOSE 8080
CMD ["python", "app.py"]
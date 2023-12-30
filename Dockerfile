# Dockerfile

FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the Python script and dependencies
COPY counter.py /app/

# Expose port 8080
EXPOSE 8080

# Start the counter program
CMD ["python", "counter.py"]


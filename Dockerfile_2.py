# Use an official lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy training script
COPY train.py .

# Create the output directory for metrics
RUN mkdir -p /output

# Ensure output directory is accessible
VOLUME ["/output"]

# Set default command
ENTRYPOINT ["python", "train.py"]

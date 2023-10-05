# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./src /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt /app

# Install any needed packages specified in requirements.txt,
RUN pip install --no-cache-dir -r /app/requirements.txt

# Make directories /mnt/output, /mnt/output/nodes, and /mnt/input in the container
RUN mkdir -p /mnt/output/nodes
RUN mkdir -p /mnt/input

# List directories to confirm they are created
RUN ls /mnt/output

# Run main.py when the container launches
ENTRYPOINT ["python", "main.py"]

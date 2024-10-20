# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /home/data

# Copy the Python script into the container at /usr/src/app
COPY script.py .
COPY IF.txt .
COPY AlwaysRememberUsThisWay.txt .

# If you have a requirements.txt file, uncomment the following line to install dependencies
# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

# Define the command to run the script
CMD ["python", "./script.py"]

# Use an official Python runtime as a parent image
FROM python:3.11.5

# Set working directory in the container
WORKDIR /app

# Copy requirements file into the container
COPY ./requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . /app

# Expose a unique port
EXPOSE 8504

# Command to run the app using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8504"]
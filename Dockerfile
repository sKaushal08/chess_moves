FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required packages for the API
RUN pip install Flask

# Expose the port the API will be running on
EXPOSE 8000

# Command to run the API when the container starts
CMD ["python", "app.py"]

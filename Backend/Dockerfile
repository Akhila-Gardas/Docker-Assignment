# Start from an official Python setup image
FROM python:3.9-slim

# Set up a workspace folder inside the box
WORKDIR /app

# Copy configuration files and install Flask
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy our app script into the box
COPY . .

# Expose port 5000 for backend data traffic
EXPOSE 5000

# Command to execute our Flask script
CMD ["python", "app.py"]
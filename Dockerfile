FROM python:3.10-slim-buster

WORKDIR /app

# Install necessary packages
RUN apt update && apt install -y supervisor

# Ensure Supervisor log directory exists
RUN mkdir -p /var/log/supervisor  

# Copy application code
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy Supervisor config file (Ensure it exists in the repo)
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  

# Expose ports
EXPOSE 8000 8501

# Start Supervisor to manage processes
CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]

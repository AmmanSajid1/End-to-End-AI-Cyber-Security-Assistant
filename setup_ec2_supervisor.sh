#!/bin/bash

# Update system and install Supervisor if not already installed
sudo apt update -y
sudo apt install -y supervisor

# Create Supervisor config for your Docker container
SUPERVISOR_CONF="/etc/supervisor/conf.d/mitre_chatbot.conf"

sudo tee $SUPERVISOR_CONF > /dev/null <<EOL
[program:mitre-chatbot]
command=docker run --rm -p 8000:8000 -p 8501:8501 --name mitre-chatbot mitre-chatbot:latest
autostart=true
autorestart=true
stderr_logfile=/var/log/mitre-chatbot.err.log
stdout_logfile=/var/log/mitre-chatbot.out.log
EOL

# Reload Supervisor configuration
sudo supervisorctl reread
sudo supervisorctl update

# Start the Supervisor program
sudo supervisorctl start mitre-chatbot

# Enable Supervisor to start on boot
sudo systemctl enable supervisor
sudo systemctl restart supervisor
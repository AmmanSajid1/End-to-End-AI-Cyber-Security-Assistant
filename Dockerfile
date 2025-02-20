FROM python:3.10-slim-buster 

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir - r requirements.txt
RUN apt update && apt install -y supervisor

RUN mkir -p /var/log/supervisor 
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf 

EXPOSE 8000 8501 

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
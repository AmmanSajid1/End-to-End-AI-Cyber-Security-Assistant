FROM python:3.10-slim-buster

WORKDIR /app 

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000 8501 

CMD ["sh", "-c", "uvicorn src.backend.main:app --host 0.0.0.0 --port 8000 & streamlit run src/ui/streamlit_app.py --server.port 8501 --server.address 0.0.0.0"]


# 🔐 AI-Powered Cybersecurity Chatbot (RAG-Based) 🛡️💬  

An **end-to-end AI-powered cybersecurity chatbot** built with **Python, FastAPI, LangChain, FAISS, and OpenAI**. This chatbot assists users with cybersecurity inquiries using **retrieval-augmented generation (RAG), natural language processing (NLP), and vector database search** to deliver accurate and contextual responses based on the **MITRE ATT&CK** framework.  

## 🛠 Tech Stack  
- **Backend:** Python, FastAPI  
- **AI & NLP:** LangChain, OpenAI API, Sentence Transformers  
- **Vector Database:** FAISS (Facebook AI Similarity Search)  
- **Document Processing:** DirectoryLoader, TextSplitter  
- **Cloud & Deployment:** AWS ECR, EC2, GitHub Actions (CI/CD), Docker  

---

## 🚀 Features  
✅ **Cybersecurity-Focused AI:** Uses LangChain & OpenAI for cybersecurity-related questions  
✅ **MITRE ATT&CK Knowledge Base:** Searches cybersecurity documents using FAISS  
✅ **FastAPI Backend:** Serves chatbot responses via a high-performance API  
✅ **CI/CD Pipeline:** Automated Docker image deployment to AWS  
✅ **Scalable & Cloud-Ready:** Runs on AWS EC2 with Dockerized architecture  

---

## 📦 Deployment Workflow  
1️⃣ **Code Push:** GitHub Actions triggers CI/CD on `main` branch updates  
2️⃣ **Docker Build & Push:** Builds and uploads the Docker image to **AWS ECR**  
3️⃣ **EC2 Deployment:** Pulls the latest image and runs it in a container  
4️⃣ **Live Chatbot:** The FastAPI server runs and serves responses on port `8000`  

---

## 🚀 Local Setup & Running the Application  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/AmmanSajid1/End-to-End-AI-Cyber-Security-Assistant.git
cd End-to-End-AI-Cyber-Security-Assistant
```

### 2️⃣ Set Up a Virtual Environment (Optional but Recommended)
Using Conda:
```bash
conda create -p venv python==3.10 -y
conda activate venv/
```

### 3️⃣ Install Dependencies 
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a ```.env``` file in the root directory and add your API keys:
```ini
OPENAI_API_KEY="your_openai_api_key
```

### 5️⃣ Scrape Cybersecurity Data from Mitre ATT&CK Website
```bash
python src/scraper/scrape_mitre.py
```

### 6️⃣ Embed and Store Cybersecurity Data in FAISS Index
```bash
python src/embeddings/embeddings.py
```

### 7️⃣ Run the Chatbot Locally

**Backend (FastAPI)**
```bash
uvicorn src.backend.main:app --host 0.0.0.0 --port 8000
```
The API will be accessible at: ```http://localhost:8000```

**Test the API using the curl example**:
```bash
curl -X POST "http://127.0.0.1:8000/search/" \
-H "Content-Type: application/json" \
-d '{"query": "What is SSL?"}'
```

**Frontend (Streamlit UI)**
```bash
streamlit run src/ui/streamlit_app.py
```
The UI will be accessible at: ```http://localhost:8501```


## 🌍 AWS Deployment with GitHub Actions (CI/CD)

### 1️⃣ AWS Setup

**1.1 Create an IAM User for Deployment**

Grant the following permissions:

 - ```AmazonEC2ContainerRegistryFullAccess``` (For AWS ECR)
 - ```AmazonEC2FullAccess``` (For EC2 Instance Management)
    Download the **Access Key and Secret Key** in a CSV file.

**1.2 Create an AWS ECR Repository**
Save the **Repository URI** for later use.

**1.3 Launch an EC2 instance (Ubuntu)**
 - Choose **Ubuntu** as the operating system.
 - Open port 8000 and 8501 in the security group to allow API and Frontend access.

**1.4 Install Docker on EC2**
Run the following commands on your EC2 instance:
```bash
sudo apt-get update -y
sudo apt-get upgrade -y
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```
**1.5 Set Up EC2 as a Self-Hosted Runner for GitHub Actions**
On GitHub, go to:
🔗 **Settings → Actions → Runners → New self-hosted runner**
Follow the commands provided and run them on your EC2 instance.

## 🔄 CI/CD Pipeline with GitHub Actions

### **GitHub Secrets Required:**
Go to **GitHub Repo → Settings → Secrets** and add the following:

 - ```AWS_ACCESS_KEY_ID``` *(from downloaded CSV)*
 - ```AWS_SECRET_ACCESS_KEY``` *(from downloaded CSV)*
 - ```AWS_DEFAULT_REGION``` *(your AWS region, e.g., us-east-1)*
 - ```ECR_REPO``` *(your AWS ECR repository name)*
 - ```OPENAI_API_KEY``` *(your OpenAI API key)*

## 📌 CI/CD Pipeline Breakdown

### 1️⃣ Continuous Integration (CI)

 - **Triggered on ```main``` branch push**
 - **Builds the Docker image**
 - **Pushes the image to AWS ECR**

### 2️⃣ Continuous Deployment (CD)

 - **Runs on EC2 self-hosted runner**
 - **Pulls the latest Docker image from ECR**
 - **Stops & removes old containers**
 - **Runs the chatbot in a new container on port ```8000``` for API and port ```8501``` for frontend (Streamlit UI)**

## 📡 API Endpoints

| **Method** | **Endpoint**   | **Description**                              |
|------------|----------------|----------------------------------------------|
| ```POST``` | ```/search/``` | Retrieve documents and generate LLM response |

## 🛠️ Technologies Used

 - FastAPI - Backend framework
 - Streamlit - Frontend UI
 - FAISS - Vector search database
 - OpenAI GPT - LLM for response generation
 - Docker - Containerization
 - AWS EC2 & ECR - Cloud deployment
 - GitHub Actions - CI/CD automation

## 📜 License
This project is **open-source** and licensed under the **MIT License**.





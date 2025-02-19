from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os 

# Change pwd to root directory
os.chdir(os.path.abspath(os.path.join(__file__ ,"../../..")))

# Load FAISS Vector Store
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_store = FAISS.load_local("data/processed/faiss_index", embedding_model, allow_dangerous_deserialization=True)

def retrieve_relevant_docs(query):
    docs = vector_store.similarity_search(query, k=5)
    return [doc.page_content for doc in docs]
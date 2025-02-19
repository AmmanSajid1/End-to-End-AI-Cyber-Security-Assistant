import os 
import faiss 
from langchain_community.vectorstores import FAISS 
from langchain_huggingface import HuggingFaceEmbeddings

# Change pwd to root directory
os.chdir(os.path.abspath(os.path.join(__file__ ,"../../..")))


def load_mitre_data():
    file_paths = [
        "data/raw/mitre_tactics.txt",
        "data/raw/mitre_techniques.txt",
        "data/raw/mitre_mitigations.txt"
    ]

    all_texts = []

    for file_path in file_paths:
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="ISO-8859-1") as f:
                all_texts.extend(f.readlines())

        else:
            print(f"Warning: {file_path} not found!")

    return [text.strip() for text in all_texts if text.strip()]


if __name__=="__main__":
    print("Started Retriever Module")
    print("\n")
    print("Loading Mitre Data")
    print("\n")
    documents = load_mitre_data()
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    print("Creating embeddings and storing in FAISS index")
    print("\n")
    vector_store = FAISS.from_texts(documents, embedding_model)
    vector_store.save_local("data/processed/faiss_index")
    print("FAISS vector store saved successfully!")


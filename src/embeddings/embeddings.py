import os 
import faiss 
from langchain_community.vectorstores import FAISS 
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader, DirectoryLoader

# Change pwd to root directory
os.chdir(os.path.abspath(os.path.join(__file__ ,"../../..")))


def load_mitre_data():
    loader = DirectoryLoader("data/raw", glob="*.txt", loader_cls=TextLoader, loader_kwargs={"encoding": "ISO-8859-1"})
    docs = loader.load()
    docs_text = [doc.page_content for doc in docs]
    return docs_text

def document_chunks(docs, chunk_size=500, chunk_overlap=50):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return text_splitter.create_documents(docs)
    


if __name__=="__main__":
    print("Started Retriever Module")
    print("\n")
    print("Loading Mitre Data")
    print("\n")
    documents = load_mitre_data()
    doc_chunks = document_chunks(documents)
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    print("Creating embeddings and storing in FAISS index")
    print("\n")
    vector_store = FAISS.from_documents(doc_chunks, embedding_model)
    vector_store.save_local("data/processed/faiss_index")
    print("FAISS vector store saved successfully!")


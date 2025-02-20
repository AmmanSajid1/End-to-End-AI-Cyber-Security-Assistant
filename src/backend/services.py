from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# Change pwd to root directory
os.chdir(os.path.abspath(os.path.join(__file__ ,"../../..")))

# Obtain OPENAI API Key from .env
load_dotenv()

# Load FAISS Vector Store
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_store = FAISS.load_local("data/processed/faiss_index", embedding_model, allow_dangerous_deserialization=True)

# Load LLM
llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0, api_key=os.getenv("OPENAI_API_KEY"))

# Define prompt template
prompt_template = PromptTemplate(
    input_variables=["context", "query"],
    template="You are a cybersecurity expert. Given the context below, answer the user's question. Don't answer from your own knowledge and only answer questions related to cybersecurity. If you don't know an answer based on the context say I don't know or if the question is not related to cybersecurity say that 'I can't answer this as I am a cybersecurity chatbot:\n\nContext:\n{context}\n\nQuery:\n{query}\n\nResponse:"
)

llm_chain = prompt_template | llm

def retrieve_and_generate_response(query):
    docs = vector_store.similarity_search(query, k=5)
    context = "\n".join([doc.page_content for doc in docs])
    
    # Generate response using LLM

    try:
        response = llm_chain.invoke({"context": context, "query": query})
        return response.content
    
    except:
        print("Error in obtaining response")
    
    
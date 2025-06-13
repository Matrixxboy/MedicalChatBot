import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from src.prompt import systemPrompt
from dotenv import load_dotenv

from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from src.helper import Hugging_face_embedding  # assuming you have it
load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GROQ_API_KEY = os.environ.get('GROQ_API_KEY')
os.environ["GROQ_API_KEY"] = GROQ_API_KEY  # or load from dotenv

llm = ChatGroq(
    model="llama3-8b-8192",  # or try "llama3-70b-8192" or "mixtral-8x7b-32768"
    temperature=0.4,
    max_tokens=500
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system",systemPrompt),
    ]
)


pc = Pinecone(api_key=PINECONE_API_KEY)
index_name = "medbot"

embedding_model = Hugging_face_embedding()  # Must match the one used to index

vectorstore = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embedding_model,
)

retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

# Create document QA chain
document_chain = create_stuff_documents_chain(llm,prompt)
chain = create_retrieval_chain(retriever, document_chain)


def chat_replay(message):
    response = chain.invoke({"input": f"{message}"})
    return response["answer"]
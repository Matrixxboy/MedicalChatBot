import os
from src.helper import load_pdf_file,text_split,Hugging_face_embedding
from pinecone import ServerlessSpec
from pinecone.grpc import PineconeGRPC as Pinecone
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
load_dotenv()

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

# ✅ New way to initialize client in v3.x
pc = Pinecone(api_key=PINECONE_API_KEY)

extracted_data = load_pdf_file(data='Data/')
text_chunks = text_split(extracted_data)
embeddings = Hugging_face_embedding()

# ✅ Create index if it doesn't exist
index_name = "medbot"

if index_name not in [index.name for index in pc.list_indexes()]:
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )
    
    
dosearch = PineconeVectorStore.from_documents(
    documents= text_chunks,
    index_name = index_name,
    embedding=embeddings,
)

print("the data is saved : ",dosearch)
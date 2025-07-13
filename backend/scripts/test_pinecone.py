import os
from dotenv import load_dotenv
from pinecone import Pinecone

# Load environment variables
load_dotenv()

# Initialize Pinecone
api_key = os.getenv("PINECONE_API_KEY")
env = os.getenv("PINECONE_ENV")
index_name = os.getenv("PINECONE_INDEX")

if not api_key or not env or not index_name:
    print("❌ Missing required environment variables.")
    exit(1)

try:
    pc = Pinecone(api_key=api_key)
    index = pc.Index(index_name)
    description = index.describe_index_stats()
    print("✅ Pinecone connection successful!")
    print(f"Index: {index_name}")
    print("Index Stats:", description)
except Exception as e:
    print("❌ Failed to connect to Pinecone:")
    print(e)

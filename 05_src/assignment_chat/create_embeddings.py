import os
from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. Load PDF
pdf_path = "./dataset/ai_report_2025.pdf"
if not os.path.exists(pdf_path):
    raise FileNotFoundError(f"PDF not found at: {pdf_path}")

loader = PyPDFLoader(pdf_path)
pages = loader.load()

full_text = ""
for p in pages:
    full_text += p.page_content + "\n"

# 2. Chunk text
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_text(full_text)
print(f"Loaded {len(chunks)} chunks from PDF")

# 3. Local embedding model
print("Encoding chunks...")
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(chunks).tolist()

# 4. ChromaDB persistent client
client = PersistentClient(path="./embeddings")
collection = client.get_or_create_collection(name="ai_report")

# 5. Store embeddings
ids = [f"chunk_{i}" for i in range(len(chunks))]
collection.add(ids=ids, documents=chunks, embeddings=embeddings)

print("✅ Embeddings created and saved in ./embeddings")

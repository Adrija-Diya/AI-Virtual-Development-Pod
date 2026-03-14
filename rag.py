from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Example knowledge base
documents = [
    "Flask is a lightweight Python web framework used to build APIs.",
    "A login API usually requires username and password validation.",
    "Python functions are defined using the def keyword.",
    "REST APIs typically return JSON responses.",
]

# Convert documents to embeddings
doc_embeddings = model.encode(documents)

# Create FAISS index
dimension = doc_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(doc_embeddings.astype("float32"))


def retrieve_context(query):

    query_embedding = model.encode([query])

    distances, indices = index.search(np.array(query_embedding), k=2)

    results = [documents[i] for i in indices[0]]

    return "\n".join(results)
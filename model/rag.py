import os

from docx import Document
from lightrag import LightRAG, QueryParam
from lightrag.llm import ollama_model_complete, ollama_embedding
from lightrag.utils import EmbeddingFunc

WORKING_DIR = "./out"

if not os.path.exists(WORKING_DIR):
    os.mkdir(WORKING_DIR)

rag = LightRAG(
    working_dir=WORKING_DIR,
    llm_model_func=ollama_model_complete,
    llm_model_name="qwen2m",
    embedding_func=EmbeddingFunc(
        embedding_dim=768,
        max_token_size=8192,
        func=lambda texts: ollama_embedding(texts, embed_model="nomic-embed-text"),
    ),
)



# Open the .docx file
doc = Document("SFWE-Graduate-Student-Handbook.docx")

# Extract the text from the .docx file
doc_text = "\n".join([para.text for para in doc.paragraphs])

# Insert the text into rag
rag.insert(doc_text)

# Perform naive search
print("Asking question 1...")
print(
    rag.query("If I have a GPA of 2.85 do I meet Satisfactory Academic Progress?", param=QueryParam(mode="local"))
)

print("Asking question 2...")
print(
    rag.query("What website should I visit to apply for Graduate Admissions?", param=QueryParam(mode="local"))
)

print("Asking question 3...")
print(
    rag.query("What are the Graduate Admission Requirements?", param=QueryParam(mode="local"))
)

print("Asking question 4...")
print(
    rag.query("What are some Electives for Software Engineering?", param=QueryParam(mode="local"))
)

# Perform local search
# print(
#     rag.query("What are the top themes in this story?", param=QueryParam(mode="local"))
# )
#
# # Perform global search
# print(
#     rag.query("What are the top themes in this story?", param=QueryParam(mode="global"))
# )
#
# # Perform hybrid search
# print(
#     rag.query("What are the top themes in this story?", param=QueryParam(mode="hybrid"))
# )
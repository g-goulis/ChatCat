import os
# from docx import Document
from lightrag import LightRAG, QueryParam
from lightrag.llm import ollama_model_complete, ollama_embedding
from lightrag.utils import EmbeddingFunc
from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
WORKING_DIR = "C:\\Users\\jmart\\Downloads\\ChatCat-ModelUpdate-main\\outi"

if not os.path.exists(WORKING_DIR):
    os.mkdir(WORKING_DIR)

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

rag = LightRAG(
    working_dir=WORKING_DIR,
    llm_model_func=ollama_model_complete,
    llm_model_name="qwen2m",

    embedding_func=EmbeddingFunc(
        embedding_dim=768,
        max_token_size=8192,
        func=lambda texts: ollama_embedding(texts, embed_model="nomic-embed-text:latest"),
    ),
)


# rag = LightRAG(
#     working_dir=WORKING_DIR,
#     llm_model_func=ollama_model_complete,
#     llm_model_name="qwen2m",
#
#     embedding_func=EmbeddingFunc(
#         embedding_dim=768,
#         max_token_size=8192,
#         func=lambda texts: ollama_embedding(texts, embed_model="nomic-embed-text:latest"),
#     ),
# )

# print("Loading text")
# doc = Document("./SFWE-Graduate-Student-Handbook.docx")
# doc_text = "\n".join([para.text for para in doc.paragraphs])
# rag.insert(doc_text)

@app.get("/ping")
async def ping():
    try:
        return "pong"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/query")
def query_model(question: str = Body(..., embed=True)):
    try:
        response =  rag.query(question, param=QueryParam(mode="hybrid"))
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

#print(rag.query("If I have a GPA of 2.85 do I meet Satisfactory Academic Progress for the graduate program?", param=QueryParam(mode="local", top_k=5)))
# Perform naive search
'''
print("Asking question 1-1...")
print(
    rag.query("If I have a GPA of 2.85 do I meet Satisfactory Academic Progress for the undergraduate program?", param=QueryParam(mode="hybrid"))
)

print("Asking question 1-2...")
print(
    rag.query("If I have a GPA of 2.85 do I meet Satisfactory Academic Progress for the graduate program?", param=QueryParam(mode="hybrid"))
)

print("Asking question 2...")
print(
    rag.query("What website should I visit to apply for Graduate Admissions?", param=QueryParam(mode="hybrid"))
)

print("Asking question 3...")
print(
    rag.query("What are the Graduate Admission Requirements?", param=QueryParam(mode="hybrid"))
)

print("Asking question 4...")
print(
    rag.query("What are some Electives for Software Engineering?", param=QueryParam(mode="hybrid"))
)

'''

from pathlib import Path
from typing import TypedDict

import chromadb
from fastapi import FastAPI
from pydantic import BaseModel
from langgraph.graph import StateGraph, END

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "chroma_db"

client = chromadb.PersistentClient(path=str(DB_PATH))
collection = client.get_or_create_collection(
    name="swiftbasket_policies"
)

app = FastAPI(
    title="SwiftBasket Customer Support Assistant",
    description="A policy document retrieval assistant for a fictional quick-commerce company."
)

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    answer: str
    sources: list[str]

class SupportState(TypedDict):
    query: str
    answer: str
    sources: list[str]

def retrieve_policy(state: SupportState):
    if collection.count() == 0:
        return {
            "answer": "The policy database is empty. Please add policy documents.",
            "sources": []
        }

    results = collection.query(
        query_texts=[state["query"]],
        n_results=min(3, collection.count())
    )

    documents = results["documents"][0] or []
    ids = results["ids"][0] or []

    if not documents:
        return {
            "answer": "Sorry, I could not find a relevant policy.",
            "sources": []
        }

    return {
        "answer": documents[0],
        "sources": ids[:1]
    }

workflow = StateGraph(SupportState)
workflow.add_node("retrieve_policy", retrieve_policy)
workflow.set_entry_point("retrieve_policy")
workflow.add_edge("retrieve_policy", END)

support_graph = workflow.compile()

@app.post("/ask", response_model=QueryResponse)
def ask_question(request: QueryRequest):
    result = support_graph.invoke({
        "query": request.query,
        "answer": "",
        "sources": []
    })

    return QueryResponse(
        answer=result["answer"],
        sources=result["sources"]
    )

@app.get("/")
def home():
    return {
        "message": "SwiftBasket Support Assistant API is running."
    }

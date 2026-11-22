# SwiftBasket – Customer Support Policy Retrieval Assistant

A semantic document retrieval assistant built for SwiftBasket, a fictional quick-commerce company. It helps retrieve relevant customer support policies based on user queries.

## Project Overview

The application uses semantic search to identify relevant policy documents and returns the matching policy text along with its source document.

## Features

- Semantic search over 8 customer support policy documents.
- Persistent vector storage using ChromaDB.
- Workflow orchestration using LangGraph.
- REST API development using FastAPI.
- Request and response validation using Pydantic.
- Docker-based application containerization.

## Tech Stack

- **Language:** Python
- **Vector Database:** ChromaDB
- **Workflow:** LangGraph
- **API Framework:** FastAPI
- **Data Validation:** Pydantic
- **Containerization:** Docker

## Project Structure

```text
support_assistant/
├── docs/
│   ├── doc_01.txt
│   ├── doc_02.txt
│   └── ... doc_08.txt
├── chroma_db/
├── 03_support_assistant.ipynb
├── main.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## API Usage

The application exposes a POST endpoint:

`/ask`

Example request:

```json
{
  "query": "What is the refund policy?"
}
```

The API returns the retrieved policy text and its source document.

## Run with Docker

Build the Docker image:

```bash
docker build -t swiftbasket-support .
```

Run the container:

```bash
docker run -p 7860:7860 swiftbasket-support
```

Open the API documentation:

`http://localhost:7860/docs`

## How It Works

1. Customer submits a question.
2. ChromaDB searches the stored policy documents using semantic similarity.
3. LangGraph manages the retrieval workflow.
4. The most relevant policy text and source are returned through FastAPI.

## Important Note

This project implements semantic document retrieval. It returns existing policy text and does not use an LLM to generate answers.

This is a learning project built around a fictional quick-commerce company.

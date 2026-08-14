# AI & ML Final Project

## Project Overview

This repository contains three modules completed as part of the AI & ML Capstone Project.

- Data Pipeline
- Analytics
- Support Assistant

Each module is organized in its own folder.

---

# Project Structure

```
ai-ml-final-project/
│
├── data_pipeline/
│   ├── 01_data_pipeline.ipynb
│   └── README.md
│
├── analytics/
│   ├── 01_eda.ipynb
│   ├── 02_modeling.ipynb
│   └── README.md
│
├── support_assistant/
│   ├── 03_support_assistant.ipynb
│   └── README.md
│
└── README.md
```

---

# Requirements

Install the required Python libraries before running the notebooks.

```
pip install pandas numpy matplotlib seaborn requests beautifulsoup4 sqlite3 chromadb sentence-transformers langgraph fastapi uvicorn
```

---

# Module 1 – Data Pipeline

This module performs data collection and preprocessing.

Main tasks:

- Scrape book information from BooksToScrape
- Clean the dataset
- Convert prices
- Store data in SQLite
- Execute SQL queries

Notebook:

```
01_data_pipeline.ipynb
```

---

# Module 2 – Analytics

This module performs exploratory data analysis and visualization.

Main tasks:

- Data loading
- Data preprocessing
- Statistical summary
- Price analysis
- Rating analysis
- Category analysis
- Visualizations

Notebooks:

```
01_eda.ipynb
02_modeling.ipynb
```

---

# Module 3 – Support Assistant

This module implements an AI-powered customer support assistant using Retrieval-Augmented Generation (RAG).

Technologies:

- ChromaDB
- Sentence Transformers
- LangGraph
- FastAPI

Main tasks:

- Semantic search
- Intent classification
- Context retrieval
- Response generation
- API endpoint

Notebook:

```
03_support_assistant.ipynb
```

---

# How to Run

## Data Pipeline

Open and run:

```
01_data_pipeline.ipynb
```

---

## Analytics

Run in order:

```
01_eda.ipynb
02_modeling.ipynb
```

---

## Support Assistant

Run:

```
03_support_assistant.ipynb
```

---

# Design Decisions

- Used modular folder structure for better organization.
- Used Pandas and SQLite for data processing.
- Used Matplotlib for visualization.
- Used ChromaDB for vector storage.
- Used Sentence Transformers for embeddings.
- Used LangGraph for workflow orchestration.
- Used FastAPI for serving the support assistant.

---

# Author

Pavan Dasari
AI & ML Capstone Project

Project completed as part of the AI & ML Capstone evaluation.

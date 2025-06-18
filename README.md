# Sparkathon Project

## Overview
This project contains a backend (FastAPI, GenAI, Pinecone), a frontend (React), and AR components. The backend integrates with Ollama for GenAI and Pinecone for vector search.

## Directory Structure

```
|-- 📂 backend/
|   |-- 📂 app/
|   |   |-- 📂 api/
|   |   |   |-- __init__.py
|   |   |   |-- 📄 chat.py             # Handles chat and GenAI interactions
|   |   |   |-- 📄 products.py         # Handles product catalog and search
|   |   |   |-- 📄 users.py            # Handles user profiles and preferences
|   |   |
|   |   |-- 📂 core/
|   |   |   |-- __init__.py
|   |   |   |-- 📄 config.py           # Configuration (e.g., Ollama URL, DB connections)
|   |   |   |-- 📄 security.py         # Authentication and security functions
|   |   |
|   |   |-- 📂 models/
|   |   |   |-- __init__.py
|   |   |   |-- 📄 product.py          # Pydantic models for products
|   |   |   |-- 📄 user.py             # Pydantic models for users
|   |   |
|   |   |-- 📂 services/
|   |   |   |-- __init__.py
|   |   |   |-- 📄 ollama_service.py   # Logic to interact with the Ollama API
|   |   |   |-- 📄 pinecone_service.py # Logic for Pinecone vector search 
|   |   |
|   |   |-- __init__.py
|   |   |-- 📄 main.py               # Main FastAPI application instance
|   |
|   |-- 📄 requirements.txt        # Python dependencies
|   |-- 📄 .env                    # Environment variables (OLLAMA_API_URL, etc.)
|   |-- 📄 .gitignore
|
|-- 📂 frontend/
|   |-- (React / React Native project structure will go here) 
|   |-- 📄 package.json
|
|-- 📂 ar/
|   |-- (AR project files using Snap AR SDK, 8th Wall, or Three.js) 
|
|-- 📂 docs/
|   |-- 📄 api_documentation.md
|   |-- 📄 project_plan.md
|
|-- 📄 README.md
```

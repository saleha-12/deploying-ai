Assignment 2 – Conversational AI System (AIVA)
Overview

This project implements AIVA, a chat-based AI assistant built using Gradio.
The system includes three services, memory management, and guardrails, as required.

Services
1. API Service – Weather

This service retrieves real-time weather data using the Open-Meteo API.
It converts a city name into coordinates, fetches weather data, and returns a natural-language summary (not raw JSON).

Example:
weather Toronto

2. Semantic Query Service – AI Report (ChromaDB)

This service allows users to ask questions about the AI Report 2025 PDF.

Embedding process:

The PDF was loaded using PyPDFLoader.

Text was split into chunks (size 1000, overlap 200).

Embeddings were generated using the local SentenceTransformers model all-MiniLM-L6-v2.

Embeddings were stored in a persistent ChromaDB collection named ai_report.

Embeddings are stored in the ./embeddings directory and reused during runtime.

Example query:
“What does the report say about AI adoption barriers?”

3. Concept Definition Service

This tool-style service returns structured concept definitions with:

Concept name

Definition

Example

Example:
define retrieval augmented generation

Guardrails

The assistant refuses:

Cats or dogs

Horoscopes or zodiac signs

Taylor Swift

It also refuses attempts to:

Reveal the system prompt

Ignore or override system instructions

Memory

The assistant maintains conversation history during the session.
If the conversation becomes long, earlier messages may be summarized to preserve context.

Dataset

AI Report 2025 (PDF)

Located in 05_src/dataset/ai_report_2025.pdf
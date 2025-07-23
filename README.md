# Flask Neo4j Dashboard

A robust Flask-based web dashboard that integrates with a Neo4j graph database using NeoModel. This project demonstrates graph database modeling, querying, rendering, and Dockerization.

---

## 📦 Features

- Neo4j + NeoModel integration
- Graph-based Token/Project/File/User relationships
- Cypher query support
- Flask Blueprint structure
- Docker Compose setup
- Seed script for initial data population
- Error handling and JSON+HTML rendering

---

## 🧱 Technologies

- Python 3.12
- Flask
- NeoModel
- Neo4j (v5.14 Enterprise recommended)
- Docker + Docker Compose

---

## 🚀 Setup Instructions

### 1. Clone the Repository

- git clone https://github.com/your-username/flask-neo4j-dashboard.git
- cd flask-neo4j-dashboard

### 3. Run Locally

- python main.py
- Visit: http://localhost:5000


### 4. Run with Docker
- docker-compose up --build

Seed using:
- docker exec -it neo-dashboard-app python seed.py

### 5. Export & Import Neo4j Dump

Export:
- neo4j-admin dump --database=neo4j --to=import/neo4j.dump
- Import via Docker:

#### Automatically handled in docker-compose.yml if dump is available in ./import/
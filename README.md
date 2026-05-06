# Tool-137: Cyber Risk Quantification Tool

## Project Overview
Tool-137 is an AI-powered web application designed to quantify cyber risks using a modern tech stack . It features real-time AI descriptions, risk recommendations, and comprehensive reporting .

## Tech Stack
* **Backend**: Java 17, Spring Boot 3.x, Spring Security + JWT .
* **AI Service**: Python 3.11, Flask, Groq API (LLaMA-3.3-70b) .
* **Frontend**: React 18+ Vite, Tailwind CSS, Axios .
* **Infrastructure**: Docker + Docker Compose, PostgreSQL 15, Redis 7 .

## Prerequisites
* Docker & Docker Compose installed .
* Java 17 (adoptium.net) .
* Python 3.11 .
* Groq API Key (console.groq.com) .

## Setup Instructions
1. **Clone the repository**: `git clone [repository-url]` .
2. **Configure Environment**: Create a `.env` file based on `.env.example`. Add your `GROQ_API_KEY` .
3. **Launch with Docker**: Run `docker-compose up --build` .
4. **Access the Tool**:
   * Frontend: `http://localhost` .
   * Backend Swagger: `http://localhost:8080/swagger-ui.html` .
   * AI Health: `http://localhost:5000/health` .

## Security Features
* **Authentication**: Secured via JWT and role-based access control .
* **Rate Limiting**: AI endpoints are limited to 30 requests per minute .
* **Sanitization**: All inputs are sanitized using the Bleach library to prevent XSS/SQLi .
* **Audit Logs**: Comprehensive logging for all Create, Update, and Delete actions .

---

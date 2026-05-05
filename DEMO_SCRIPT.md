# AI Demo Script — Tool-137
# Demo Day: 9 May 2026

---

## My Section (60 seconds)

### Opening Line:
"Our AI service runs on Flask, powered by Groq API
using LLaMA-3.3-70b-versatile model."

---

## Live Demo Steps

### Step 1 — Show /health endpoint (10 seconds)
Run:
curl http://localhost:5000/health

Say:
"This is our health endpoint — it shows the AI model,
uptime, and average response time."

---

### Step 2 — Show /describe endpoint (15 seconds)
Run:
curl -X POST http://localhost:5000/describe \
-H "Content-Type: application/json" \
-d '{"asset_name": "Web Server",
     "asset_type": "Server",
     "description": "Public facing server with no firewall"}'

Say:
"Here we send an asset to our AI — it returns
a risk level, risk score, vulnerabilities and impact.
Response time is around 2 seconds."

---

### Step 3 — Show /recommend endpoint (15 seconds)
Run:
curl -X POST http://localhost:5000/recommend \
-H "Content-Type: application/json" \
-d '{"asset_name": "Web Server",
     "asset_type": "Server",
     "description": "Public facing server with no firewall",
     "risk_level": "Critical"}'

Say:
"Now we get 3 actionable recommendations —
each with an action type and priority level."

---

### Step 4 — Explain tech stack (10 seconds)
Say:
"We use Flask for the API, Groq for the AI model,
bleach for input sanitisation, and flask-limiter
for rate limiting at 30 requests per minute."

---

### Step 5 — Security explanation (10 seconds)
Say:
"Every input is sanitised to strip HTML and block
prompt injection. All Groq calls have 3-retry backoff
and return a fallback if the AI is unavailable.
Full details in our SECURITY.md."

---

## Q&A Answers

Q: What AI model are you using?
A: LLaMA-3.3-70b-versatile via Groq API — free tier,
   no credit card required.

Q: What security measures are in place?
A: Input sanitisation with bleach, prompt injection
   detection, rate limiting at 30 req/min, Redis cache,
   and 4 security headers on every response.

Q: What happens if the AI is unavailable?
A: Every Groq call has 3-retry with exponential backoff.
   If all retries fail, we return a fallback response
   with is_fallback: true so the app never crashes.

Q: How fast is the AI?
A: /health: 7ms, /describe: 2.4s, /recommend: 0.8s

---

## Backup Screenshots
If live demo fails, show these screenshots:
1. /health
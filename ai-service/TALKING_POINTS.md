# AI Talking Points Card
# Tool-137 — Demo Day 9 May 2026

---

## What AI model are we using?
LLaMA-3.3-70b-versatile via Groq API
- Free tier, no credit card required
- Fast inference speed
- Strong reasoning for security analysis

---

## What does the AI service do?
3 endpoints:
1. /describe — analyses an asset and returns risk level,
   risk score, vulnerabilities and business impact
2. /recommend — returns 3 actionable security
   recommendations with priority levels
3. /health — shows model, uptime, response time

---

## How do prompts work?
- Prompt templates stored in prompts/ folder
- Asset details injected into template at runtime
- AI returns structured JSON every time
- Temperature set to 0.3 for consistent factual output

---

## What security measures are in place?
- bleach strips HTML from all inputs
- Injection patterns detected and blocked (400 error)
- Rate limiting: 30 requests/minute per IP
- Redis cache: 15 min TTL (SHA256 key)
- 3-retry with exponential backoff on Groq failures
- Fallback response if AI is unavailable

---

## Performance
- /health: ~7ms
- /describe: ~2.4s
- /recommend: ~0.8s

---

## What happens if Groq is down?
- 3 retries with backoff (1s, 2s, 4s)
- If all fail: returns fallback response
- is_fallback: true in response
- App never crashes or returns 500

---

## Security Q&A
Q: Is any personal data sent to Groq?
A: No — PII audit confirmed, only asset
   technical details sent

Q: How is the API key protected?
A: Stored in .env file, never committed to GitHub

Q: What if someone sends malicious input?
A: bleach sanitises it, injection patterns
   blocked with 400 error
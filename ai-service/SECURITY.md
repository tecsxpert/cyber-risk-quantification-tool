# Security Documentation — AI Service
# Tool-137 Cyber Risk Quantification Tool

## Threat Model

### Threat 1: Prompt Injection
- Description: Attacker manipulates AI prompts to bypass security
- Risk: High
- Mitigation: Input sanitisation, injection pattern detection
- Test: Sent "ignore previous instructions" as input
- Result: PASS — 400 error returned, request blocked

### Threat 2: API Key Exposure
- Description: Groq API key accidentally committed to GitHub
- Risk: High
- Mitigation: Store in .env file, .env added to .gitignore
- Test: Checked git status, verified .env not tracked
- Result: PASS — .env not visible in repository

### Threat 3: Rate Limit Abuse
- Description: Attacker floods endpoints with requests
- Risk: Medium
- Mitigation: flask-limiter set to 30 requests/minute per IP
- Test: Sent 35 requests in sequence
- Result: PASS — requests 31-35 returned 429

### Threat 4: SQL Injection
- Description: Malicious SQL sent in input fields
- Risk: Medium
- Mitigation: bleach sanitisation strips dangerous characters
- Test: Sent "test; DROP TABLE risks;--" as input
- Result: PASS — input blocked

### Threat 5: Excessive Data Exposure
- Description: AI response leaks sensitive internal data
- Risk: Medium
- Mitigation: PII audit on all prompts, no personal data sent to Groq
- Test: Reviewed all prompt templates
- Result: PASS — no PII in any prompt

## Security Tests — Week 1
| Test | Endpoint | Input | Result |
|------|----------|-------|--------|
| Empty input | /describe | {} | PASS |
| SQL injection | /describe | DROP TABLE | PASS |
| Prompt injection | /describe | ignore previous instructions | PASS |
| Empty input | /recommend | {} | PASS |
| SQL injection | /recommend | DROP TABLE | PASS |
| Prompt injection | /recommend | ignore previous instructions | PASS |

## Residual Risks
- Redis not yet configured for rate limiting
- JWT validation pending
- OWASP ZAP scan pending Day 7

## Team Sign-off
- AI Developer 2: Yashaswini — Week 1 security tests completed
## OWASP ZAP Scan — Day 7
- ZAP automated scan attempted on http://localhost:5000
- Manual security headers verification performed via curl
- All 4 security headers confirmed present and working:
  - X-Content-Type-Options: nosniff ✅
  - X-Frame-Options: DENY ✅
  - Content-Security-Policy: default-src 'self' ✅
  - X-XSS-Protection: 1; mode=block ✅
- Zero Critical findings
- Zero High findings
- Status: PASS
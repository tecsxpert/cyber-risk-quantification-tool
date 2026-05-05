import bleach
import re

INJECTION_PATTERNS = [
    r"ignore previous instructions",
    r"you are now",
    r"forget your prompt",
    r"act as",
    r"jailbreak",
    r"<script",
    r"drop table",
    r"' or '1'='1",
]

def sanitize_input(text: str) -> str:
    return bleach.clean(str(text), strip=True)

def detect_injection(text: str) -> bool:
    lowered = text.lower()
    return any(re.search(p, lowered) for p in INJECTION_PATTERNS)

def validate_and_sanitize(data: dict, required_fields: list):
    for field in required_fields:
        if field not in data:
            return None, f"Missing field: {field}"
        data[field] = sanitize_input(data[field])
        if detect_injection(data[field]):
            return None, f"Invalid input detected in field: {field}"
    return data, None
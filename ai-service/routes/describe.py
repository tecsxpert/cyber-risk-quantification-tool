from flask import Blueprint, request, jsonify
from datetime import datetime
from services.groq_client import GroqClient
from routes.middleware import validate_and_sanitize

describe_bp = Blueprint('describe', __name__)
client = GroqClient()

@describe_bp.route('/describe', methods=['POST'])
def describe():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    data, error = validate_and_sanitize(data, ['asset_name', 'asset_type', 'description'])
    if error:
        return jsonify({"error": error}), 400

    with open("prompts/describe_prompt.txt", "r") as f:
        prompt_template = f.read()

    prompt = prompt_template.format(**data)

    messages = [{"role": "user", "content": prompt}]
    result = client.call(messages)

    if result is None:
        return jsonify({
            "risk_level": "Unknown",
            "risk_score": 0,
            "description": "AI service temporarily unavailable",
            "vulnerabilities": [],
            "impact": "Unknown",
            "generated_at": datetime.now().isoformat(),
            "is_fallback": True
        }), 200

    import json
    try:
        parsed = json.loads(result)
        parsed["generated_at"] = datetime.now().isoformat()
        return jsonify(parsed), 200
    except json.JSONDecodeError:
        return jsonify({"error": "Failed to parse AI response"}), 500
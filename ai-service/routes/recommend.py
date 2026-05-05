from flask import Blueprint, request, jsonify
from services.groq_client import GroqClient
from routes.middleware import validate_and_sanitize
import json

recommend_bp = Blueprint('recommend', __name__)
client = GroqClient()

@recommend_bp.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    data, error = validate_and_sanitize(data, ['asset_name', 'asset_type', 'description', 'risk_level'])
    if error:
        return jsonify({"error": error}), 400

    with open("prompts/recommend_prompt.txt", "r") as f:
        prompt_template = f.read()

    prompt = prompt_template.format(**data)
    messages = [{"role": "user", "content": prompt}]
    result = client.call(messages)

    if result is None:
        return jsonify([
            {
                "action_type": "review",
                "description": "AI service temporarily unavailable. Please review security manually.",
                "priority": "High",
                "is_fallback": True
            }
        ]), 200

    try:
        parsed = json.loads(result)
        return jsonify(parsed), 200
    except json.JSONDecodeError:
        return jsonify({"error": "Failed to parse AI response"}), 500
from flask import Blueprint, jsonify
import time
import os

health_bp = Blueprint('health', __name__)

START_TIME = time.time()
request_times = []

@health_bp.route('/health', methods=['GET'])
def health():
    uptime_seconds = int(time.time() - START_TIME)
    hours = uptime_seconds // 3600
    minutes = (uptime_seconds % 3600) // 60
    seconds = uptime_seconds % 60

    avg_response_time = (
        sum(request_times) / len(request_times)
        if request_times else 0
    )

    return jsonify({
        "status": "healthy",
        "model": "llama-3.3-70b-versatile",
        "uptime": f"{hours}h {minutes}m {seconds}s",
        "avg_response_time_ms": round(avg_response_time, 2),
        "total_requests": len(request_times)
    }), 200
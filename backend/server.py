from flask import Flask, jsonify, request
from backend.langgraph_agent import MasterAgent

backend_app = Flask(__name__)

@backend_app.route('/health_article', methods=['POST'])
def generate_article():
    data = request.json
    master_agent = MasterAgent()
    article = master_agent.run(data["topic"])
    return jsonify({"path": article}), 200


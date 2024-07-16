from flask import Flask, jsonify, request
from backend.langgraph_agent import MasterAgent

backend_app = Flask(__name__)

@backend_app.route('/generate_tweets', methods=['POST'])
def generate_newspaper():
    data = request.json
    master_agent = MasterAgent()
    tweets = master_agent.run(data["topic"])
    return jsonify({"tweets": tweets}), 200


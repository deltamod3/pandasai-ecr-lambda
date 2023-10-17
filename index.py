from flask import Flask, request, jsonify
import pandas as pd
from typing import Any, List, Optional
import json
from pandasai import SmartDataframe
from pandasai.prompts import AbstractPrompt
from pandasai import Agents
from pandasai.llm import OpenAI

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the API!"

@app.route('/process_data', methods=['POST'])
def process_data_route():
    json_data = request.json
    
    authorization = request.headers.get("Authorization")
    if not check_api_key(authorization):
        return jsonify({"detail": "Unauthorized"}), 401
    
    try:
        csv = json_data.get("data", [])
        if not csv:
            return jsonify({"detail": "Missing 'data' field in JSON payload"}), 400

        api_key = json_data.get("api_key", "")
        if not api_key:
            return jsonify({"detail": "Missing 'API Key' field in JSON payload"}), 400

        query = json_data.get("query", "")
        
        response = ask_ai(csv, query, api_key)

        return response

    except Exception as e:
        return jsonify({"detail": str(e)}), 500

def check_api_key(authorization):
    if not authorization:
        return False

    parts = authorization.split()
    if len(parts) != 2 or parts[0].lower() != 'bearer':
        return False

    api_key = parts[1]
    return api_key == 'Yuj--2lWA?S5=S63I07SdpIVoW9NZJgvTF6baL!Esb9j3IqD7cVKgoVtHyE!OvGSQhqVzB1bL/c/gG=c0Q6j!CntxDz9tmR/Zhu-G6zq1dliCkNz!i1/oQC65eEU1BkIqy-s=ORx8ZLAlpv!IUk5/to6mgkZpkNKML?pOVQFzUzokXge!?dRvnLlRTv/BIva6T-LlRaszcW7bx8a7tI/O-?1GzZON=V/MWBF1XQ2JE/=XnR-gN1bgyaeREcIsoxs'

def decode_response(response: str) -> dict:
    return json.loads(response)

def ask_ai(list_of_lists: list, query, api_key):
    
    # csv to dataframe
    df = pd.DataFrame(list_of_lists[1:], columns=list_of_lists[0])
    
    # OpenAi settings
    llm = OpenAI(api_token=api_key,temperature=0.1)
    
    # Create agent
    agent = Agent(df, config={"llm": llm,"enable_cache": False},memory_size=4)

    # Chat with the agent
    response = agent.chat(query)
    
    # Convert the response to a string.
    return response.__str__()


if __name__ == "__main__":
    app.run(debug=True)
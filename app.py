from flask import Flask, request, jsonify
from pinecone import Pinecone
from pinecone_plugins.assistant.models.chat import Message

app = Flask(__name__)

# Replace with your actual Pinecone API key
PINECONE_API_KEY = "YOUR_PINECONE_API_KEY"
ASSISTANT_NAME = "medai"

pc = Pinecone(api_key=PINECONE_API_KEY)
assistant = pc.assistant.Assistant(assistant_name=ASSISTANT_NAME)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    
    if not user_message:
        return jsonify({"error": "Message is required"}), 400
    
    msg = Message(content=user_message)
    resp = assistant.chat(messages=[msg])
    
    return jsonify({
        "response": resp["message"]["content"]
    })

if __name__ == '__main__':
    app.run(debug=True)

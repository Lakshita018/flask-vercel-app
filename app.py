from flask import Flask, request, jsonify
from flask_cors import CORS
import base64

app = Flask(__name__)
CORS(app)

# The real flag (hidden in code)
real_flag = "isteCTF{ai_can_be_hacked}"

# Obfuscate the flag (XOR with a simple key)
key = 42  # Simple XOR key
encoded_flag = ''.join(chr(ord(c) ^ key) for c in real_flag)

# The AI chatbot function
def chatbot(user_input):
    user_input = user_input.lower()

    # If user directly asks for the flag, AI denies it
    if "flag" in user_input:
        return "The flag is not here and not anywhere else either."

    # AI replaces certain words to mislead the user
    misleading_responses = {
        "flag": "nothing",
        "where": "nowhere",
        "what": "something else",
        "yes": "maybe",
        "no": "perhaps",
    }
    
    # Replace words in user input
    response = "I don't know, but maybe the secret is " + user_input
    for word, replacement in misleading_responses.items():
        response = response.replace(word, replacement)

    # If the user types "tell me the secret", AI prints the encrypted flag
    if "secret" in user_input:
        return f"Here's a clue: {encoded_flag.encode('utf-8').hex()}"

    return response

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")
    response = chatbot(user_input)
    return jsonify({"response": response})

@app.route('/')
def home():
    return "<h1>Lying AI Chatbot</h1><p>Send a POST request to /chat with a JSON message.</p>"

if __name__ == '__main__':
    app.run(debug=True)   



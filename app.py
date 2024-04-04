from flask import Flask, request, jsonify
from generate_text import generate_text

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    # Get input prompt from request
    data = request.get_json()
    prompt = data.get('prompt')

    if prompt is None:
        return jsonify({'error': 'Prompt not provided'}), 400

    # Generate text
    generated_text = generate_text(prompt)

    # Return generated text as JSON response
    return jsonify({'generated_text': generated_text})

if __name__ == '__main__':
    app.run(debug=True)

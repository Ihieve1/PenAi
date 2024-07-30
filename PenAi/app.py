from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Initialize the text generation pipeline
generator = pipeline('text-generation', model='gpt2')

def generate_email_with_ai(data):
    prompt = f"Write an email with the following details:\n"
    prompt += f"Subject: {data['subject']}\n"
    prompt += f"To: {data['recipient']}\n"
    prompt += f"From: {data['sender']}\n"
    prompt += f"Tone: {data['tone']}\n"
    prompt += f"Language: {data['language']}\n"
    
    if 'receivedEmail' in data:
        prompt += f"In response to: {data['receivedEmail']}\n"

    # Generate text
    result = generator(prompt, max_length=int(data['length']) * 10, num_return_sequences=1)

    # The generated text is in result[0]['generated_text']
    generated_email = result[0]['generated_text']

    # Remove the prompt from the generated text
    generated_email = generated_email.replace(prompt, '')

    return generated_email.strip()

@app.route('/generate_email', methods=['POST'])
def generate_email():
    data = request.json
    try:
        generated_email = generate_email_with_ai(data)
        return jsonify({"email": generated_email})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
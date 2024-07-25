from flask import Flask, request, jsonify
import requests
import openai

app = Flask(__name__)

# Set your API keys here
MAILGUN_API_KEY = 'YOUR_MAILGUN_API_KEY'
MAILGUN_DOMAIN = 'YOUR_MAILGUN_DOMAIN'
OPENAI_API_KEY = 'YOUR_OPENAI_API_KEY'

openai.api_key = OPENAI_API_KEY

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.json
    recipient = data.get('recipient')
    subject = data.get('subject')
    sender = data.get('sender')
    tone = data.get('tone')
    language = data.get('language')
    received_email = data.get('received_email', '')

    # Generate email content using OpenAI
    email_content = generate_email_content(recipient, subject, sender, tone, language, received_email)

    # Send email using Mailgun
    response = send_mailgun_email(recipient, subject, sender, email_content)

    return jsonify({'message': 'Email sent successfully!', 'response': response})

def generate_email_content(recipient, subject, sender, tone, language, received_email):
    prompt = f"""
    Compose an email with the following details:
    Recipient: {recipient}
    Subject: {subject}
    Sender: {sender}
    Tone: {tone}
    Language: {language}
    Received Email: {received_email}
    """
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=500
    )
    email_content = response.choices[0].text.strip()
    return email_content

def send_mailgun_email(recipient, subject, sender, content):
    return requests.post(
        f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
        auth=("api", MAILGUN_API_KEY),
        data={"from": sender,
              "to": [recipient],
              "subject": subject,
              "text": content})

if __name__ == '__main__':
    app.run(debug=True)

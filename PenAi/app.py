from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

MAILGUN_DOMAIN = 'your_mailgun_domain'
MAILGUN_API_KEY = 'your_mailgun_api_key'

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.json
    recipient = data['recipient']
    subject = data['subject']
    body = data['body']

    response = requests.post(
        f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
        auth=("api", MAILGUN_API_KEY),
        data={"from": "Excited User <mailgun@YOUR_DOMAIN_NAME>",
              "to": [recipient],
              "subject": subject,
              "text": body})

    return jsonify({'status': 'success' if response.status_code == 200 else 'error'})

if __name__ == '__main__':
    app.run(debug=True)

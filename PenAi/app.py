from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

my_key = os.getenv("API_KEY")

genai.configure(api_key=my_key)

defaults = {
  'model': 'models/chat-bison-001',
  'temperature': 0.25,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
}

context = "Given a topic, write emails in a concise, professional manner"
examples = [
  [
    "Request vacation time next week",
    "Dear [Manager's name],\n\nI am writing to request vacation time from [start date] to [end date]. I will be using my accrued vacation time for this trip.\n\nI have already completed all of my current projects and tasks, and I have made arrangements for my colleagues to cover my responsibilities while I am away. I will be available by email and phone if needed.\n\nI am looking forward to this time to relax and recharge. I will be back in the office on [return date].\n\nThank you for your approval.\n\nSincerely,\n[Your name]"
  ],
  [
    "Make it shorter",
    "Dear [Manager's name],\n\nI am writing to request vacation from [start date] to [end date]. I have completed all of my current projects and tasks, and I have made arrangements for my colleagues to cover my responsibilities. I will be available by email and phone if needed.\n\nThank you for your approval.\n\nSincerely,\n[Your name]"
  ]
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    user_input = request.form["user_input"]
    messages = [user_input]
    response = genai.chat(
        **defaults,
        context=context,
        examples=examples,
        messages=messages
    )
    return jsonify({'response': response.last})


if __name__ == '__main__':
    app.run(debug=True)

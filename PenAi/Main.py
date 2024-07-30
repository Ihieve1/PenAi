import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import pyperclip

load_dotenv()

penai = os.getenv('API_KEY')

genai.configure(api_key=penai)

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
messages = []

# Gets user input for email 
def get_user_input():
  topic = st.text_input("Enter the topic of your email:")
  tone = st.selectbox("Choose a tone", ["formal", "informal", "friendly"])
  length = st.selectbox("Choose the length", ["short", "medium", "long"])
  recipient = st.text_input("Enter the recipient's email address:")
  return topic, tone, length, recipient

# Generates an email based on user input
def generate_email(topic, tone, length): 
  global messages 
  messages.append(f"NEXT REQUEST: Write an email about {topic} in a {tone} tone. Make it {length}.")
  response = genai.chat(
    **defaults,
    context=context,
    examples=examples,
    messages=messages
  )
  return response.last

# copy_to_clipboard
def copy_to_clipboard(text): 
  pyperclip.copy(text)
  st.success("Email copied to clipboard!")

def main():
  st.title("Pen Ai")
  topic, tone, length, recipient = get_user_input()
  
  if st.button("Generate Email"):
    email_text = generate_email(topic, tone, length)
    st.markdown(f"Generated email:\n{email_text}")

    # Add a copy button
    if st.button("Copy to Clipboard"):
      copy_to_clipboard(email_text)

if __name__ == "__main__":
  main()

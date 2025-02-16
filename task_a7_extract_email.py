import os
import openai

# Set up OpenAI API key from environment variable
api_key = "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" 
openai.api_key = api_key
openai.api_base = "https://api.openai.com/v1"

# Read email content
with open('email.txt', 'r', encoding='utf-8') as f:
    email_content = f.read()

# Ask GPT-4o-Mini to extract the sender’s email
prompt = f"Extract the sender's email address from the following email content:\n\n{email_content}\n\nOnly return the email address, nothing else."

response = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    messages=[{"role": "system", "content": "You are an expert at extracting information from emails."},
              {"role": "user", "content": prompt}],
    max_tokens=50
)

# Extract result
email_address = response['choices'][0]['message']['content'].strip()

# Write to output file
output_path = 'email-sender.txt'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(email_address)

print(f"Extracted sender email: {email_address}")
print(f"Email address written to {output_path}")

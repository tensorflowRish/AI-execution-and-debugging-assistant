from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

print("AI Debugging Assistant")

error_input = input("\ntype in your error message:\n")

prompt = f"""
You are an AI debugging assistant.

Analyze the following error and provide:

1. Root cause
2. Step-by-step fix
3. Prevention advice

Error:
{error_input}
"""

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print("\nAI Analysis\n")
print(response.choices[0].message.content)
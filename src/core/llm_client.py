import os 
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class LLMClient:
    def __init__(self):
        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )
    
    def ask(self, prompt):
        response = self.client.chat.completions.create(
            model = "llama-3.1-8b-instant",
            messages = [
                {
                    "role" : "user",
                    "content" : prompt
                }
            ]
        )

        return response.choices[0].message.content
from groq import Groq
class LLMClient:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)
        self.model = "llama-3.1-8b-instant"
    def generate(self, prompt):
        try:
            chat = self.client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model=self.model, temperature=0.1
            )
            return chat.choices[0].message.content
        except Exception as e: return f"Error: {str(e)}"

from ollama import generate
from config import MODEL_NAME

class RealTimeChat:
    def __init__(self):
        self.history = []
        self.system_prompt = """You're a helpful AI assistant. 
        Provide concise, accurate responses to user queries."""

    def respond(self, user_input):
        response = generate(
            model=MODEL_NAME,
            prompt=user_input,
            system=self.system_prompt,
            context=self.history[-4:] if self.history else [],
            stream=False
        )
        self.history.append((user_input, response['response']))
        return response['response']

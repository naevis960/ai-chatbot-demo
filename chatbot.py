import openai
import json
from typing import List, Dict, Optional


class ChatBot:
    def __init__(
        self,
        model: str = "gpt-4",
        system_prompt: str = "You are a helpful assistant.",
        language: str = "en",
        max_history: int = 20,
    ):
        self.model = model
        self.system_prompt = system_prompt
        self.language = language
        self.max_history = max_history
        self.history: List[Dict[str, str]] = []
        self.client = openai.OpenAI()

    def chat(self, message: str) -> str:
        self.history.append({"role": "user", "content": message})

        if len(self.history) > self.max_history:
            self.history = self.history[-self.max_history:]

        messages = [{"role": "system", "content": self.system_prompt}] + self.history

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.7,
        )

        reply = response.choices[0].message.content
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def reset(self):
        self.history = []

    def save_history(self, filename: str = "chat_history.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.history, f, ensure_ascii=False, indent=2)

    def load_history(self, filename: str = "chat_history.json"):
        with open(filename, "r", encoding="utf-8") as f:
            self.history = json.load(f)


if __name__ == "__main__":
    bot = ChatBot(system_prompt="You are a friendly assistant that speaks Japanese.")
    print("ChatBot ready! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            bot.save_history()
            break
        response = bot.chat(user_input)
        print(f"Bot: {response}")

# 🤖 AI Chatbot Demo

An intelligent chatbot powered by OpenAI API with multi-language support.

## Features
- 💬 Natural conversation with GPT-4 / GPT-3.5
- 🌍 Multi-language support (Japanese, English, etc.)
- 🧠 Context-aware responses with memory
- 🔧 Customizable system prompts
- 📝 Conversation logging
- 🔌 Easy API integration

## Quick Start

```bash
pip install -r requirements.txt
export OPENAI_API_KEY="your-key"
python chatbot.py
```

## Usage

```python
from chatbot import ChatBot

bot = ChatBot(
    model="gpt-4",
    system_prompt="You are a helpful assistant.",
    language="ja"
)

response = bot.chat("Hello!")
print(response)
```

## License
MIT

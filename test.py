from dotenv import load_dotenv
load_dotenv()
import anthropic
print(anthropic.Anthropic().messages.create(
    model="claude-sonnet-4-6", max_tokens=16,
    messages=[{"role": "user", "content": "hi"}],
).content[0].text)
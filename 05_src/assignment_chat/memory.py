from openai import OpenAI
import os

client = OpenAI(
    base_url="https://k7uffyg03f.execute-api.us-east-1.amazonaws.com/prod/openai/v1",
    api_key="any value",
    default_headers={"x-api-key": "YOUR_GATEWAY_KEY_HERE"}   # CHANGE THIS
)

def summarize_memory(history):
    """
    Summarize old parts of the conversation when memory grows too long.
    """
    text = "\n".join([f"User: {h['user']}\nAI: {h['assistant']}" for h in history])

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": f"Summarize the following:\n{text}"}
        ]
    )

    return response.choices[0].message.content

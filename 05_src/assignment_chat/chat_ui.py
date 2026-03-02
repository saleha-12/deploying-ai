import gradio as gr
from openai import OpenAI

from api_service import get_weather
from semantic_service import semantic_query
from concept_service import define_concept
from guardrails import violates_guardrails
from memory import summarize_memory
from intent_classifier import classify_intent

client = OpenAI(
    base_url="https://k7uffyg03f.execute-api.us-east-1.amazonaws.com/prod/openai/v1",
    api_key="any value",
    default_headers={"x-api-key": "NI1Ma8b7myE4oYPvQyx3"}   
)

chat_history = []

SYSTEM_PROMPT = "You are AIVA, a friendly AI assistant."

def chat_fn(message):
    global chat_history

    if violates_guardrails(message):
        return "Sorry, I'm not allowed to discuss that."

    intent = classify_intent(message)

    if intent == "weather":
        city = message.replace("weather", "").strip()
        reply = get_weather(city)

    elif intent == "semantic":
        reply = semantic_query(message)

    elif intent == "concept":
        concept = message.replace("define", "").replace("explain", "").strip()
        info = define_concept(concept)
        reply = f"{info['concept']}:\n{info['definition']}\nExample: {info['example']}"

    else:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": message}
            ]
        )
        reply = response.choices[0].message.content

    chat_history.append({"user": message, "assistant": reply})

    if len(chat_history) > 10:
        summary = summarize_memory(chat_history[:-5])
        chat_history = [{"user": "summary", "assistant": summary}] + chat_history[-5:]

    return reply

def launch_ui():
    gr.Interface(
        fn=chat_fn,
        inputs=gr.Textbox(label="Ask something"),
        outputs=gr.Textbox(label="AIVA replies:"),
        title="AIVA Chat Assistant"
    ).launch()

import gradio as gr
from app.services.llm_service import ask_ai


def chat(message, history):
    response = ask_ai(message)

    return response


interface = gr.ChatInterface(
    fn=chat,
    title="Airline AI Assistant",
    description="Ask about airline ticket prices"
)


interface.launch()
import gradio as gr
from app.services.llm_service import ask_ai


def chat(message, history):
    response = ask_ai(message)

    if response is None:
        return "Sorry, I could not generate a response. Please try again."


    return response


interface = gr.ChatInterface(
    fn=chat,
    title="Airline AI Assistant",
    description="Ask about airline ticket prices"
)


interface.launch()
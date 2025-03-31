from chatbot import ChatBot
import gradio as gr
from config import MODEL_NAME

chatbot = ChatBot()

def respond(message, history):
    response = chatbot.generate_response(message)
    history.append((message, response))
    return "", history

with gr.Blocks(title="Local ChatGPT") as demo:
    gr.Markdown(f"## Local ChatGPT using {MODEL_NAME}")
    
    with gr.Row():
        chatbot = gr.Chatbot(height=500)
        txt = gr.Textbox(placeholder="Type your message...", scale=3)
        
    clear = gr.ClearButton([txt, chatbot])

    txt.submit(
        respond,
        [txt, chatbot],
        [txt, chatbot]
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", share=False)

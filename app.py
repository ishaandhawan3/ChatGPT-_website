from chatbot import RealTimeChat
import gradio as gr

chat = RealTimeChat()

def process_message(message, history):
    response = chat.respond(message)
    history.append((message, response))
    return "", history

with gr.Blocks(title="Real-Time Chat") as demo:
    gr.Markdown("## Live Chat Interface")
    
    with gr.Row():
        chat_interface = gr.Chatbot(height=500)
        msg = gr.Textbox(label="Your Message")
        
    clear_btn = gr.ClearButton([msg, chat_interface])

    msg.submit(
        process_message,
        [msg, chat_interface],
        [msg, chat_interface]
    )

if __name__ == "__main__":
    demo.launch()

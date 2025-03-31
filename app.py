import gradio as gr
from ollama import generate
import time

class EnhancedChat:
    def __init__(self):
        self.history = gr.State([])
        self.system_msg = """You're a helpful AI assistant. 
        Respond clearly and concisely to user queries."""

    def respond(self, message, chat_history):
        try:
            # Add user message to history
            updated_history = chat_history + [[message, None]]
            
            # Generate streaming response
            response = generate(
                model="gemma:2b",
                prompt=message,
                system=self.system_msg,
                stream=True
            )
            
            # Stream bot response
            bot_message = ""
            for chunk in response:
                token = chunk['response']
                bot_message += token
                updated_history[-1][1] = bot_message
                yield updated_history, ""
            
            # Final update to preserve response
            yield updated_history, ""
            
        except Exception as e:
            error_msg = f"⚠️ Error: {str(e)}"
            updated_history = chat_history + [[message, error_msg]]
            return updated_history, ""

# Create interface
with gr.Blocks(theme=gr.themes.Soft(), css=".message {max-width: 80%; margin: 10px auto;}") as demo:
    chat = EnhancedChat()
    
    gr.Markdown("## 🤖 Local ChatGPT Clone")
    gr.Markdown("_Powered by Ollama and Gradio_")
    
    with gr.Row():
        chatbot = gr.Chatbot(
            elem_id="chatbot",
            bubble_full_width=False,
            show_copy_button=True,
            avatar_images=(
                "https://example.com/user.png", 
                "https://example.com/bot.png"
            )
        )
        
    with gr.Row():
        msg = gr.Textbox(
            scale=4,
            placeholder="Type your message...",
            container=False,
            autofocus=True
        )
        submit_btn = gr.Button("Send", variant="primary", scale=1)
        clear_btn = gr.ClearButton([msg, chatbot], value="🗑️ Clear")

    # Event handling
    msg.submit(
        chat.respond,
        [msg, chat.history],
        [chatbot, msg],
        queue=False
    ).then(lambda: None, None, None, preprocess=False)

    submit_btn.click(
        chat.respond,
        [msg, chat.history],
        [chatbot, msg],
        queue=False
    )

if __name__ == "__main__":
    demo.launch(server_port=7860)

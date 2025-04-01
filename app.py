import gradio as gr
from ollama import generate

class EnhancedChat:
    def __init__(self):
        self.history = []  # Stores conversation history as OpenAI-style dictionaries
        self.system_msg = "You're a helpful AI assistant. Respond clearly and concisely to user queries."

    def respond(self, message, chat_history):
        try:
            # Add user message to history
            chat_history.append({"role": "user", "content": message})
            
            # Generate response from the model
            response = generate(
                model="gemma:2b",
                prompt=message,
                system=self.system_msg,
                stream=False  # Disable streaming for simplicity
            )
            
            # Add assistant's response to history
            chat_history.append({"role": "assistant", "content": response['response']})
            
            return chat_history, ""
        
        except Exception as e:
            # Handle errors gracefully
            error_msg = f"⚠️ Error: {str(e)}"
            chat_history.append({"role": "assistant", "content": error_msg})
            return chat_history, ""

# Create interface
with gr.Blocks(css="style.css") as demo:
    chat = EnhancedChat()
    
    gr.Markdown("## 🤖 Local ChatGPT Clone")
    gr.Markdown("_Created by Ishaan Dhawan_")
    
    chatbot = gr.Chatbot(type="messages")  # Use OpenAI-style messages format
    
    with gr.Row():
        msg = gr.Textbox(
            placeholder="Type your message...",
            container=False,
            autofocus=True,
        )
        submit_btn = gr.Button("Send", variant="primary")
        clear_btn = gr.Button("Clear Chat", variant="secondary")

    # Event handling
    submit_btn.click(
        chat.respond,
        [msg, chatbot],
        [chatbot, msg]
    )
    
    msg.submit(
        chat.respond,
        [msg, chatbot],
        [chatbot, msg]
    )
    
    clear_btn.click(
        lambda: ([], ""),  # Clear the chat history and input box
        inputs=[],
        outputs=[chatbot, msg]
    )

if __name__ == "__main__":
    demo.launch(share=True)

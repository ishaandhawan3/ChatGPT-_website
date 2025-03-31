This is a lightweight, locally hosted chatbot application inspired by ChatGPT. It uses Gradio for the user interface and Ollama for running a local language model. The chatbot provides real-time responses to user prompts while maintaining conversation history. The project is designed to be simple, efficient, and privacy-focused, as it runs entirely on your local machine.


✨ Features

Real-Time Chat: Interact with the chatbot in real time.


Local Execution: No data is sent to external servers; everything runs on your PC.


Lightweight Model: Uses Ollama's lightweight models like gemma:2b for fast and efficient responses.


Customizable UI: A clean and simple interface with a translucent gray background and black text.


Conversation History: Maintains the context of the conversation.


🚀 How to Use This Project

1. Clone the Repository
First, clone this repository to your local machine:


bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
2. Install Dependencies
Make sure you have Python 3.8+ installed on your system. Then, create a virtual environment and install the required dependencies:


bash
# Create a virtual environment
python -m venv venv


# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate


# Install dependencies
pip install -r requirements.txt
3. Install Ollama
This project uses Ollama to run the language model locally. Follow these steps to set up Ollama:


Download and install Ollama from their official website.


Once installed, pull the lightweight model (e.g., gemma:2b) using:


bash
ollama pull gemma:2b
4. Run the Application
Run the app using the following command:


bash
python app.py
This will start a local server (default: http://127.0.0.1:7860) where you can interact with your chatbot.


🛠️ How to Use It on Your Own PC from GitHub
If someone wants to use this chatbot from your GitHub repository, they can follow these steps:


Clone Your Repository:


bash
git clone https://github.com/ishaandhawan3/ChatGPT-_website
cd ChatGPT-_website
Install Python and Dependencies:
Make sure they have Python 3.8+ installed, then install dependencies as described above.


Install Ollama and Pull a Model:
They need to install Ollama and pull a compatible model (e.g., gemma:2b).


Run the Application:
Start the app using:


bash
python app.py
Access the Chatbot:
Open their browser and go to http://127.0.0.1:7860 to interact with the chatbot.


📂 Project Structure
Here’s an overview of the project files:


text
my-chatgpt-project/
├── app.py                # Main application code for running the chatbot
├── requirements.txt      # List of dependencies for the project
└── style.css             # Custom CSS for styling (optional)
📋 Requirements
Python 3.8+


Gradio (pip install gradio)


Ollama (https://ollama.ai/)


Lightweight language model (e.g., gemma:2b)


🌟 Customization
Change Background Image or Colors
To customize the chatbot's appearance, edit the custom_css section in app.py. For example:


To change the background image, replace the URL in background-image.


To adjust colors, modify properties like background-color or color.


❓ FAQ
Q: Can I use a different model?
Yes! You can use any lightweight model supported by Ollama. Just replace gemma:2b with another model name when pulling it via ollama pull.


Q: Does this work offline?
Yes! Since everything runs locally on your machine, no internet connection is required after setting up.


👏 Acknowledgments
This project uses:

Gradio for building the user interface.

Ollama for running local language models.

Feel free to fork this repository and customize it as needed! 😊

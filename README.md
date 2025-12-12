🤖 AI Personal Assistant - Ollama Chatbot
A beautiful, customizable AI chatbot interface built with Streamlit and Ollama, featuring real-time streaming responses and multiple personality modes.
✨ Features

🎨 Modern UI Design - Elegant gradient interface with smooth animations
🎭 Multiple Personality Modes - Choose from Friendly, Professional, Creative, Technical, or Custom personalities
🔧 Customizable Parameters - Adjust temperature, max tokens, and streaming speed
💬 Real-time Streaming - Watch AI responses appear character by character
📊 Conversation Statistics - Track your messages and AI responses
💾 Save Conversations - Export chat history to text files
🔄 Model Selection - Switch between different Ollama models (phi3, llama2, mistral, gemma)
⚡ Responsive Design - Clean, user-friendly interface with emoji avatars

🚀 Quick Start
Prerequisites

Python 3.8 or higher
Ollama installed and running

Installation

Clone the repository

bashgit clone https://github.com/yourusername/ai-personal-assistant.git
cd ai-personal-assistant

Create a virtual environment

bashpython3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies

bashpip install -r requirements.txt

Download Ollama models

bashollama pull phi3
# Optional: Download other models
ollama pull llama2
ollama pull mistral

Run the application

bashstreamlit run AI_andreas.py

Open your browser at http://localhost:8501

📦 Dependencies
streamlit>=1.28.0
ollama>=0.1.0
🎮 Usage
Personality Modes

Friendly: Warm, conversational, and empathetic responses
Professional: Clear, concise, and well-structured answers
Creative: Imaginative responses with metaphors and innovative approaches
Technical: Detailed, precise answers with code examples when relevant
Custom: Define your own AI personality

Model Parameters

Temperature (0.0-2.0): Controls creativity vs. predictability
Max Tokens (100-2000): Sets maximum response length
Stream Speed (0.01-0.5s): Adjusts text display speed

Keyboard Shortcuts

Enter: Send message
Ctrl + C: Stop the application (in terminal)


🛠️ Configuration
The application can be customized by modifying the following in AI_andreas.py:

Available Models: Edit the available_models list
Personality Prompts: Modify the personality_prompts dictionary
UI Colors: Change the gradient colors in the CSS section
Default Parameters: Adjust slider default values

📝 Project Structure
ai-personal-assistant/
│
├── AI_andreas.py          # Main application file
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── .gitignore            # Git ignore file
└── screenshots/          # Application screenshots

🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

Fork the project
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request

🐛 Known Issues

Ollama must be running before starting the application
Model download may take time depending on internet connection
First response from a model may be slower as it loads into memory

📋 Roadmap

 Add support for image inputs
 Implement conversation search functionality
 Add dark/light theme toggle
 Support for multiple conversation threads
 Export conversations in multiple formats (JSON, PDF)
 Add voice input/output capabilities

🔒 Privacy
This application runs entirely locally on your machine. No data is sent to external servers except for downloading Ollama models.
📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
👨‍💻 Author
Andreas Mara

GitHub: @Mustangul14
Email: andymara669@gmail.com

🙏 Acknowledgments

Streamlit - The web framework used
Ollama - Local LLM runtime
Inspired by modern chat interfaces and AI assistants
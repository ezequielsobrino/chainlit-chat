# Chat with Chainlit

This project implements a chatbot using the Groq API and Chainlit for the user interface. The chatbot allows users to interact with various language models provided by Groq, with customizable settings.

## Features

- Multiple model options (llama3-8b-8192, llama3-70b-32768, mixtral-8x7b-32768, gemma-7b-it, gemma2-9b-it)
- Adjustable settings:
  - Model selection
  - Token streaming
  - Temperature
  - Max tokens
- Conversation history management
- Real-time response streaming

## Technologies Used

### Chainlit

This project uses Chainlit to create an interactive chat interface. Chainlit is a powerful tool for building Python-based chatbots and AI applications with ease.

For more information and documentation on Chainlit, visit:
[Chainlit GitHub Repository](https://github.com/Chainlit/chainlit)

### Groq API

The chat functionality is powered by Groq's language models. Groq provides fast and efficient AI inference capabilities.

For a quick start guide and API documentation, visit:
[Groq API Quickstart](https://console.groq.com/docs/quickstart)

## Prerequisites

- Python 3.7+
- Groq API key (Sign up at [console.groq.com](https://console.groq.com/) if you haven't already)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/ezequielsobrino/chainlit-chat.git
   cd chainlit-chat
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory of the project and add your Groq API key:
   ```bash
   echo GROQ_API_KEY=your_api_key_here > .env
   ```

   Replace `your_api_key_here` with your actual Groq API key.

## Usage

Run the Chainlit app:

```bash
chainlit run app.py
```

Open your web browser and navigate to `http://localhost:8000` to interact with the chatbot.

## Configuration

You can adjust the chatbot settings using the UI controls provided by Chainlit:

- Model: Choose from available Groq models
- Streaming: Toggle token streaming on/off
- Temperature: Adjust the randomness of the model's output
- Max Tokens: Set the maximum number of tokens for the model to generate

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Additional Resources

- [Chainlit Documentation](https://docs.chainlit.io)
- [Groq API Reference](https://console.groq.com/docs/api-reference)
- [Groq Python Client Library](https://github.com/groq/groq-python)

For any issues or questions specific to Chainlit or Groq, please refer to their respective documentation or support channels.
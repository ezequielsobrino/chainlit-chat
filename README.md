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

## Prerequisites

- Python 3.7+
- Groq API key

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/ezequielsobrino/chainlit-chat.git
   cd chainlit-chat
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Groq API key as an environment variable:
   ```
   export GROQ_API_KEY=your_api_key_here
   ```

## Usage

Run the Chainlit app:

```
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
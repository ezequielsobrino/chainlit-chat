import os
import chainlit as cl
from chainlit.input_widget import Select, Switch, Slider
from groq import AsyncGroq

client = AsyncGroq(api_key=os.environ.get("GROQ_API_KEY"))


@cl.on_chat_start
async def start():
    settings = await cl.ChatSettings(
        [
            Select(
                id="Model",
                label="Groq - Model",
                values=[
                    "llama3-8b-8192",
                    "llama3-70b-8192",
                    "mixtral-8x7b-32768",
                    "gemma-7b-it",
                    "gemma2-9b-it",
                ],
                initial_index=0,
            ),
            Switch(id="Streaming", label="Groq - Stream Tokens", initial=True),
            Slider(
                id="Temperature",
                label="Groq - Temperature",
                initial=0.5,
                min=0,
                max=2,
                step=0.1,
            ),
            Slider(
                id="Max_Tokens",
                label="Groq - Max Tokens",
                initial=1024,
                min=1,
                max=32768,
                step=1,
                description="Maximum number of tokens to generate.",
            ),
        ]
    ).send()

    cl.user_session.set("model", "llama3-8b-8192")
    cl.user_session.set("streaming", True)
    cl.user_session.set("temperature", 0.5)
    cl.user_session.set("max_tokens", 1024)

    cl.user_session.set("conversation_history", [
        {"role": "system", "content": "You are a helpful assistant."}
    ])


@cl.on_settings_update
async def setup_agent(settings):
    print("on_settings_update", settings)
    for key, value in settings.items():
        cl.user_session.set(key, value)


@cl.on_message
async def main(message: cl.Message):
    model = cl.user_session.get("model")
    streaming = cl.user_session.get("streaming")
    temperature = cl.user_session.get("temperature")
    max_tokens = cl.user_session.get("max_tokens")

    conversation_history = cl.user_session.get("conversation_history")

    conversation_history.append({"role": "user", "content": message.content})

    stream = await client.chat.completions.create(
        messages=conversation_history,
        model=model,
        temperature=temperature,
        max_tokens=max_tokens,
        stream=streaming,
    )

    msg = cl.Message(content="")

    full_response = ""
    if streaming:
        async for chunk in stream:
            content = chunk.choices[0].delta.content
            if content:
                full_response += content
                await msg.stream_token(content)
        await msg.send()
    else:
        response = await stream
        full_response = response.choices[0].message.content
        await cl.Message(content=full_response).send()

    conversation_history.append({"role": "assistant", "content": full_response})

    cl.user_session.set("conversation_history", conversation_history)
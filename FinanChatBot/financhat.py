# First importing model from langchain_ollama
from langchain_ollama import ChatOllama


# Instantiating the model with the specified parameters
chatmodel = ChatOllama(
    model="qwen2.5:latest",
    temperature=0.8,
    system_prompt="You are a helpful assistant who gives info to the users.",
    # other params ...
)

response = chatmodel.invoke("What is the current stock price of Apple Inc.?")
print(response)




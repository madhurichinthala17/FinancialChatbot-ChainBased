# First importing model from langchain_ollama
from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Instantiating the model with the specified parameters
chatmodel = ChatOllama(
    model="qwen2.5:latest",
    temperature=0.8,
    # other params ...
)
# prompt_template = ChatPromptTemplate.from_messages([
#     ("system", "You are a helpful assistant who gives info to the users."),
#     ("human", "{input}") ])

# #without chaining
# prompt = prompt_template.invoke(input="Advantages of using MachineLearning ?")

# response = chatmodel.invoke(prompt)

# print(response)

# chain = prompt_template | chatmodel | StrOutputParser()
# response = chain.invoke(input="Advantages of using MachineLearning ?")
# print(response)

#invocing the agent with a message
#always in a dictionary
#response = agent.invoke({"messages" : [HumanMessage("What is the current stock price of Apple Inc.?")]})
#Because AI Message is always the last response
#print(response["messages"][-1].content)




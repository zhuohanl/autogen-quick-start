from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient
import asyncio
import os
from dotenv import load_dotenv

# Define a tool
async def get_weather(city: str) -> str:
    return f"The weather in {city} is 73 degrees and Sunny."


async def main() -> None:
    
    # Get configuration settings 
    load_dotenv()
    azure_oai_endpoint = os.getenv("AZURE_OAI_ENDPOINT")
    azure_oai_key = os.getenv("AZURE_OAI_KEY")
    azure_oai_deployment = os.getenv("AZURE_OAI_DEPLOYMENT")
    azure_oai_model = os.getenv("AZURE_OAI_MODEL")


    # Define an agent
    weather_agent = AssistantAgent(
        name="weather_agent",
        # model_client=OpenAIChatCompletionClient(
        #     model="gpt-4o-2024-08-06",
        #     # api_key="YOUR_API_KEY",
        # ),
        model_client=AzureOpenAIChatCompletionClient(
            azure_deployment=azure_oai_deployment,
            model=azure_oai_model,
            api_version="2024-06-01",
            azure_endpoint=azure_oai_endpoint,
            # azure_ad_token_provider=token_provider,  # Optional if you choose key-based authentication.
            api_key=azure_oai_key, # For key-based authentication.
        ),
        tools=[get_weather],
    )

    # Define a team with a single agent and maximum auto-gen turns of 1.
    agent_team = RoundRobinGroupChat([weather_agent], max_turns=1)

    while True:
        # Get user input from the console.
        user_input = input("Enter a message (type 'exit' to leave): ")
        if user_input.strip().lower() == "exit":
            break
        # Run the team and stream messages to the console.
        stream = agent_team.run_stream(task=user_input)
        await Console(stream)


# NOTE: if running this inside a Python script you'll need to use asyncio.run(main()).
# await main()
asyncio.run(main())
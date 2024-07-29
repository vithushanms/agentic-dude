# Standard imports
import os

# Third party imports
from dotenv import load_dotenv

# Internal dependencies
from agents.react_agent import get_agent

load_dotenv(os.path.join("..", ".env"))

prompt = input("Enter your query (or type exit to quite): ")
while prompt != "exit":
    result = get_agent().query(prompt)
    print(result)
    prompt = input("Enter your query (or type exit to quite): ")

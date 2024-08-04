# Standard imports
import os

# Third party imports
from dotenv import load_dotenv

# Internal dependencies
from agents.react_agent import get_agent

load_dotenv(os.path.join("..", ".env"))

filenames = input ("Place the files you want to use and enter the names here to slect (seperate it with coma ',' if multiple): ")
prompt = input("\n Enter your query (or type exit to quite): ")
while prompt != "exit":
    result = get_agent(context_documents=filenames).query(prompt)
    print(result)
    prompt = input("Enter your query (or type exit to quite): ")

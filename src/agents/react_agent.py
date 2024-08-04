# Thrid party imports
from llama_index.core.agent import ReActAgent

# Internal dependencies
from dudes import create_query_dude_engine, create_summary_dude_engine
from configs.llm import get_openai_model

llm = get_openai_model()

# dudes
tools = [
    create_summary_dude_engine()
]

def get_agent(context_documents: str, verbose: bool = True) -> ReActAgent:
    documentsArray = context_documents.split(",")

    for document in documentsArray:
        tools.append(create_query_dude_engine(llm=llm, file_name=document))

    return ReActAgent(llm=llm, tools=tools, verbose=verbose, memory=[])

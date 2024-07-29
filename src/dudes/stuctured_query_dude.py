"""
A tool that helps to perform query on suctured data
"""

# Standard imports
import os

# Thrid party imports
from dotenv import load_dotenv
from llama_index.core.tools import QueryEngineTool, ToolMetadata
import pandas as pd
from llama_index.experimental.query_engine import PandasQueryEngine
from llama_index.core.agent import ReActAgent

# Internal dependencies
from configs.promts import get_prompt_template, get_instructions
from utils.file_system import read_file_as_dataframe


def create_query_dude_engine(
    llm, file_name: str, verbose: bool = True
) -> QueryEngineTool:
    pandas_query_engine = PandasQueryEngine(
        df=read_file_as_dataframe("../storage/" + file_name),
        verbose=verbose,
        instruction_str=get_instructions(),
        llm=llm,
    )
    pandas_query_engine.update_prompts({"pandas_prompt": get_prompt_template()})

    return QueryEngineTool(
        query_engine=pandas_query_engine,
        metadata=ToolMetadata(
            name="query_dude",
            description="Perform query on structured data",
        ),
    )

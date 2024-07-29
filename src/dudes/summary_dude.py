"""
A tool that helps to write the summary in a file
"""

# Third pary imports
from llama_index.core.tools import FunctionTool

# Internal dependencies
from utils.file_system import save_file


def write_summary(title: str, summary: str) -> None:
    save_file(f"{title}.txt", summary)


def create_summary_dude_engine():
    return FunctionTool.from_defaults(
        fn=write_summary,
        name="summary_dude",
        description="Store the summary in a file",
    )

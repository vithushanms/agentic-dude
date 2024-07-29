from llama_index.core import PromptTemplate


def get_instructions():
    return """\
        1. Convert the query to executable Python code using Pandas.
        2. The final line of code should be a Python expression that can be called with the `eval()` function.
        3. The code should represent a solution to the query.
        4. PRINT ONLY THE EXPRESSION.
        5. Do not quote the expression.
        """


def get_prompt_template():
    return PromptTemplate(
        """\
        You are working with a pandas dataframe in Python.
        The name of the dataframe is `df`.
        This is the result of `print(df.head())`:
        {df_str}

        Follow these instructions:
        {instruction_str}
        Query: {query_str}

        Expression: """
    )
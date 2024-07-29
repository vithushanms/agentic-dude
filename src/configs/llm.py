# Third party imports
from llama_index.llms.openai import OpenAI

# Internal dependencies
from configs.env_config import OPENAI_API_KEY


def get_openai_model(model_name: str = "gpt-3.5-turbo") -> OpenAI:
    return OpenAI(model_name=model_name, api_key=OPENAI_API_KEY)

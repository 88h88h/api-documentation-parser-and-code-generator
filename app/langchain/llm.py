from langchain_openai import ChatOpenAI
import langchain
import os
langchain.verbose = False
langchain.debug = False
langchain.llm_cache = False
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model='gpt-4o', api_key=os.getenv("KEY"))

def get_llm_response(documentation: str, query: str) -> dict:
    prompt = prompt = f"""
Read the following API documentation and identify the required API endpoint, its parameter, headers and response format according to the user query:

API Documentation:
{documentation}

User Query:
{query}

Please return the response as a dictionary (and nothing else) with the following keys:
- 'endpoint': The required API endpoint based on the user query.
- 'param': The parameters required for the endpoint.
- 'headers': The headers for the endpoint.
- 'response_format': The response format for the endpoint.
"""

    response = llm.invoke(prompt)
    return response

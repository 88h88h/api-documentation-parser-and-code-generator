from langchain.llm import llm


def generate_code(parsed_docs: dict, query: str) -> str:
    endpoint = parsed_docs.get("endpoint")
    params = parsed_docs.get("params")
    headers = parsed_docs.get("headers")

    prompt = (
    f"""
Generate Python code to call the API endpoint '{endpoint}' 
using the requests library with the following details:
- Parameters: {params}
- Headers: {headers}
- Query: '{query}'

The generated code should include:
- Constructing the URL with the endpoint and query parameters
or 
- Constructing the URL and then the body for the endpoint
- Setting up the headers
- Making the API request (GET or POST as appropriate) using requests library of python
- Handling the response and printing it out

Only write the code to call the api as the response and nothing else
"""
)

    response = llm.invoke(prompt)
    return response

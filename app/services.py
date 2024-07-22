from langchain.llm import get_llm_response
from langchain.code_generation import generate_code
from langchain.data_handling import parse_and_store_response

def process_request(documentation: str, query: str):
    parsed_docs = get_llm_response(documentation, query)
    generated_code = generate_code(parsed_docs, query)
    validation_result = parse_and_store_response(generated_code)
    print(validation_result)
    return generated_code

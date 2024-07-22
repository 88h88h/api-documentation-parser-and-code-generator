from fastapi import APIRouter
from models import APIDocs
from services import process_request

router = APIRouter()

@router.get("/")
def main():
    return "Welcome to Advanced API Documentation Parser"

@router.post("/generate_code/")
async def generate_code(api_docs: APIDocs):
    response = process_request(api_docs.documentation, api_docs.query)
    return {"code": response}

from pydantic import BaseModel

class APIDocs(BaseModel):
    documentation: str
    query: str

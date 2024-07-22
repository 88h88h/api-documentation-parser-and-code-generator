import pandas as pd
import json
import requests

def parse_and_store_response(response: str, file_name: str = "response.csv") -> str:
    try:
        data = json.loads(response)
        df = pd.DataFrame(data)
        df.to_csv(file_name, index=False)
        return "Data stored successfully in response.csv"
    except Exception as e:
        return f"Failed to store data: {str(e)}"

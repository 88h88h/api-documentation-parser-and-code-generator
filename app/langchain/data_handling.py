import pandas as pd
import json
import requests

def parse_and_store_response(code: str, file_name: str = "response.csv") -> str:
    try:
        # Run the code

        #
        response = {}
        # store the response in response

        data = json.loads(response)
        df = pd.DataFrame(data)
        df.to_csv(file_name, index=False)
        return "Data stored successfully in response.csv"
    except Exception as e:
        return f"Failed to store data: {str(e)}"

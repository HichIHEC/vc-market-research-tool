import requests

class APIClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.serper.dev"

    def make_request(self, endpoint, params=None):
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def search(self, query):
        endpoint = "search"
        params = {
            "q": query,
            "num": 10
        }
        return self.make_request(endpoint, params)
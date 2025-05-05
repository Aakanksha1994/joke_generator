import requests

class JokeGenerator:
    def __init__(self):
        self.api_url = "https://v2.jokeapi.dev/joke/Any"

    def get_joke(self):
        try:
            response = requests.get(self.api_url)
            if response.status_code == 200:
                data = response.json()
                return data.get("joke", "No joke found")
            return None
        except Exception as e:
            print(f"Error fetching joke: {e}")
            return None

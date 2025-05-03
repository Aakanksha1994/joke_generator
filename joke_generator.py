import requests
import json
from typing import Optional

class JokeGenerator:
    def __init__(self):
        self.used_jokes = set()
        self.api_url = "https://v2.jokeapi.dev/joke/Any"

    def get_joke(self) -> Optional[str]:
        try:
            response = requests.get(self.api_url)
            data = response.json()
            
            if data["type"] == "single":
                joke = data["joke"]
            else:
                joke = f"{data['setup']}\n{data['delivery']}"
            
            if joke not in self.used_jokes:
                self.used_jokes.add(joke)
                return joke
            else:
                return self.get_joke()  # Try again if joke was already used
                
        except Exception as e:
            print(f"Error fetching joke: {e}")
            return None

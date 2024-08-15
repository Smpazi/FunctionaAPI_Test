import requests


class WebApiPage:
    def __init__(self, base_URL):
        self.base_URL = base_URL

    def get_response(self, endpoint):
        url = f"{self.base_URL}{endpoint}"
        response = requests.get(url)
        return response

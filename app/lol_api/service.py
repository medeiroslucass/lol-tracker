import requests

class LeagueAPIClient:
    _instance = None
    BASE_URL = 'https://{region}.api.riotgames.com'
    API_KEY = 'RGAPI-993dce0c-6fb1-4ab8-845c-b35418bcdae1'
    API_URL = BASE_URL + '?api_key=' + API_KEY

    def __new__(cls, region):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.region = region
            cls._instance.session = requests.Session()
        return cls._instance

    def request(self, endpoint, params=None):
        url = f"{self.API_URL}/{endpoint}"
        response = self.session.get(url, params=params)
        response.raise_for_status()  # Lança uma exceção se a resposta não for bem-sucedida
        return response.json()


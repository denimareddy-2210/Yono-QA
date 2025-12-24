import requests
import uuid
from utils.config import BASE_URL, PUBLIC_API_KEY, PRIVATE_SECRET_KEY

class APIClient:

    @staticmethod
    def headers():
        return {
            "public-api-key": PUBLIC_API_KEY,
            "private-secret-key": PRIVATE_SECRET_KEY,
            "x-idempotency-key": str(uuid.uuid4()),
            "Content-Type": "application/json"
        }

    @staticmethod
    def post(endpoint, payload):
        return requests.post(
            f"{BASE_URL}{endpoint}",
            json=payload,
            headers=APIClient.headers()
        )

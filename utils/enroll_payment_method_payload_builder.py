from utils.config import ACCOUNT_ID

def enroll_card_payload():
    return {
        "account_id": ACCOUNT_ID,
        "country": "AR",
        "type": "CARD",
        "workflow": "DIRECT",
        "card_data": {
            "number": "4507990000000002",
            "expiration_month": "11",
            "expiration_year": "2028",
            "cvv": "123",
            "cardholder_name": "Denima Reddy"
        }
    }

from utils.config import ACCOUNT_ID

def verify_payment_payload():
    return {
        "account_id": ACCOUNT_ID,
        "description": "VERIFY",
        "merchant_order_id": "VERIFY-001",
        "workflow": "DIRECT",
        "verify": True,
        "amount": {"value": 0, "currency": "USD"},
        "additional_data": {"country": "AR"},
        "payment_method": {
            "type": "CARD",
            "detail": {
                "card": {
                    "number": "4507990000000002",
                    "expiration_month": "11",
                    "expiration_year": "2028",
                    "cvv": "123"
                }
            }
        }
    }

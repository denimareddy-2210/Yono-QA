from utils.config import ACCOUNT_ID

def successful_single_step_payment():
    return {
        "account_id": ACCOUNT_ID,
        "description": "SUCCEEDED",
        "merchant_order_id": "ORDER-001",
        "workflow": "DIRECT",
        "amount": {"value": 1000, "currency": "USD"},
        "additional_data": {"country": "AR"},
        "payment_method": {
            "type": "CARD",
            "detail": {
                "card": {
                    "number": "4507990000000002",
                    "expiration_month": "11",
                    "expiration_year": "2028",
                    "cvv": "123",
                    "capture": True
                }
            }
        }
    }

def authorization_payment():
    payload = successful_single_step_payment()
    payload["merchant_order_id"] = "ORDER-AUTH-001"
    payload["payment_method"]["detail"]["card"]["capture"] = False
    return payload

def insufficient_funds_payment():
    payload = successful_single_step_payment()
    payload["description"] = "INSUFFICIENT_FUNDS"
    payload["payment_method"]["detail"]["card"]["number"] = "4507990000000010"
    return payload

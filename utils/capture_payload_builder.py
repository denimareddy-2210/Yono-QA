def full_capture_payload():
    return {
        "merchant_reference": "CAPTURE-001",
        "amount": {"value": 1000, "currency": "USD"},
        "reason": "PRODUCT_CONFIRMED",
        "simplified_mode": False
    }

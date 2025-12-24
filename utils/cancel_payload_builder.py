def cancel_payment_payload():
    return {
        "description": "Cancelled by customer",
        "reason": "REQUESTED_BY_CUSTOMER",
        "merchant_reference": "CANCEL-001"
    }

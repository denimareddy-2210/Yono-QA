from behave import when
from utils.api_client import APIClient
from utils.verify_payload_builder import verify_payment_payload

@when("I verify a card payment")
def step_verify_payment(context):
    context.response = APIClient.post(
        "/payments",
        verify_payment_payload()
    )

@when("I verify a card payment with invalid card")
def step_verify_invalid(context):
    payload = verify_payment_payload()
    payload["payment_method"]["detail"]["card"]["number"] = "4507990000000051"
    context.response = APIClient.post("/payments", payload)

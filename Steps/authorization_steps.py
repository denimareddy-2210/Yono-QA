from behave import when
from utils.api_client import APIClient
from utils.payload_builder import authorization_payment

@when("I create an authorization payment")
def step_create_authorization(context):
    context.response = APIClient.post(
        "/payments",
        authorization_payment()
    )

@when("I create an authorization with insufficient funds")
def step_auth_insufficient(context):
    payload = authorization_payment()
    payload["payment_method"]["detail"]["card"]["number"] = "4507990000000010"
    context.response = APIClient.post("/payments", payload)

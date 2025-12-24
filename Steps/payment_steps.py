from behave import when
from utils.api_client import APIClient
from utils.payload_builder import (
    successful_single_step_payment,
    insufficient_funds_payment
)

@when("I create a successful payment")
def step_successful_payment(context):
    context.response = APIClient.post(
        "/payments",
        successful_single_step_payment()
    )

@when("I create a payment with insufficient funds")
def step_insufficient_funds(context):
    context.response = APIClient.post(
        "/payments",
        insufficient_funds_payment()
    )

@when("I create a payment with invalid CVV")
def step_invalid_cvv(context):
    payload = successful_single_step_payment()
    payload["payment_method"]["detail"]["card"]["number"] = "4507990000000044"
    context.response = APIClient.post("/payments", payload)

@when("I create a payment without account id")
def step_missing_account_id(context):
    payload = successful_single_step_payment()
    payload.pop("account_id")
    context.response = APIClient.post("/payments", payload)

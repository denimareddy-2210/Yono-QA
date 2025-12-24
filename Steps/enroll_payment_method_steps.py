from behave import when
from utils.api_client import APIClient
from utils.enroll_payment_method_payload_builder import enroll_card_payload

@when("I enroll a card payment method for the customer")
def step_enroll_card(context):
    context.response = APIClient.post(
        f"/customers/{context.customer_id}/payment-methods",
        enroll_card_payload()
    )

@when("I enroll the same card again")
def step_enroll_same_card(context):
    context.response = APIClient.post(
        f"/customers/{context.customer_id}/payment-methods",
        enroll_card_payload()
    )

@when("I enroll a payment method with invalid customer id")
def step_enroll_invalid_customer(context):
    context.response = APIClient.post(
        "/customers/invalid-id/payment-methods",
        enroll_card_payload()
    )

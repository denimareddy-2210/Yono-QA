from behave import when
from utils.api_client import APIClient
from utils.cancel_payload_builder import cancel_payment_payload

@when("I cancel the authorized payment")
def step_cancel_payment(context):
    context.response = APIClient.post(
        f"/payments/{context.payment_id}/transactions/{context.transaction_id}/cancel",
        cancel_payment_payload()
    )

@when("I cancel payment with invalid transaction id")
def step_cancel_invalid(context):
    context.response = APIClient.post(
        f"/payments/{context.payment_id}/transactions/invalid-id/cancel",
        cancel_payment_payload()
    )

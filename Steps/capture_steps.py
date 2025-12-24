from behave import when
from utils.api_client import APIClient
from utils.capture_payload_builder import full_capture_payload, partial_capture_payload

@when("I capture the authorized payment")
def step_full_capture(context):
    context.response = APIClient.post(
        f"/payments/{context.payment_id}/transactions/{context.transaction_id}/capture",
        full_capture_payload()
    )

@when("I partially capture the authorized payment")
def step_partial_capture(context):
    context.response = APIClient.post(
        f"/payments/{context.payment_id}/transactions/{context.transaction_id}/capture",
        partial_capture_payload()
    )

@when("I capture payment with invalid transaction id")
def step_invalid_capture(context):
    context.response = APIClient.post(
        f"/payments/{context.payment_id}/transactions/invalid-id/capture",
        full_capture_payload()
    )

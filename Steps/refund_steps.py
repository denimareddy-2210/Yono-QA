from behave import when
from utils.api_client import APIClient
from utils.refund_payload_builder import full_refund_payload, partial_refund_payload

@when("I create a full refund")
def step_full_refund(context):
    context.response = APIClient.post(
        f"/payments/{context.payment_id}/transactions/{context.transaction_id}/refunds",
        full_refund_payload()
    )

@when("I create a partial refund")
def step_partial_refund(context):
    context.response = APIClient.post(
        f"/payments/{context.payment_id}/transactions/{context.transaction_id}/refunds",
        partial_refund_payload()
    )

@when("I create a refund with invalid transaction id")
def step_invalid_refund(context):
    context.response = APIClient.post(
        f"/payments/{context.payment_id}/transactions/invalid-id/refunds",
        full_refund_payload()
    )

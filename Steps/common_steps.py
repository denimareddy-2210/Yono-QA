from behave import given
from utils.api_client import APIClient
from utils.payload_builder import authorization_payment
from utils.capture_payload_builder import full_capture_payload
from utils.refund_payload_builder import full_refund_payload
from utils.customer_payload_builder import minimal_customer_payload

@given("an authorized payment exists")
def step_authorized_payment(context):
    res = APIClient.post("/payments", authorization_payment())
    context.payment_id = res.json()["id"]
    context.transaction_id = res.json()["transactions"][0]["id"]

@given("a captured payment exists")
def step_captured_payment(context):
    step_authorized_payment(context)
    APIClient.post(
        f"/payments/{context.payment_id}/transactions/{context.transaction_id}/capture",
        full_capture_payload()
    )

@given("a refunded payment exists")
def step_refunded_payment(context):
    step_captured_payment(context)
    APIClient.post(
        f"/payments/{context.payment_id}/transactions/{context.transaction_id}/refunds",
        full_refund_payload()
    )

@given("a customer exists")
def step_customer_exists(context):
    res = APIClient.post("/customers", minimal_customer_payload())
    context.customer_id = res.json()["id"]

@given("a card is already enrolled")
def step_card_enrolled(context):
    from utils.enroll_payment_method_payload_builder import enroll_card_payload
    APIClient.post(
        f"/customers/{context.customer_id}/payment-methods",
        enroll_card_payload()
    )

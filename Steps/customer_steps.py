from behave import when
from utils.api_client import APIClient
from utils.customer_payload_builder import (
    minimal_customer_payload,
    full_customer_payload
)

@when("I create a customer with minimal data")
def step_create_min_customer(context):
    context.response = APIClient.post(
        "/customers",
        minimal_customer_payload()
    )

@when("I create a customer with full data")
def step_create_full_customer(context):
    context.response = APIClient.post(
        "/customers",
        full_customer_payload()
    )

@when("I create a customer with missing mandatory fields")
def step_create_invalid_customer(context):
    context.response = APIClient.post("/customers", {})

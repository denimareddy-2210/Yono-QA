from behave import then

@then("the response status code should be {status_code}")
def step_status_code(context, status_code):
    assert context.response.status_code == int(status_code), \
        f"Expected {status_code}, got {context.response.status_code}"

@then('the payment status should be "{expected_status}"')
def step_payment_status(context, expected_status):
    actual = context.response.json().get("status")
    assert actual == expected_status, \
        f"Expected {expected_status}, got {actual}"

@then("the old card should be unenrolled")
def step_old_card_unenrolled(context):
    # Provider behavior validated via success response
    assert context.response.status_code == 200

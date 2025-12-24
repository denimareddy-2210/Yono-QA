Feature: Purchase Payment (Single-Step)

  @sanity @integration
  Scenario: Successful card payment
    When I create a successful payment
    Then the response status code should be 201
    And the payment status should be "SUCCEEDED"

  @regression
  Scenario: Payment declined due to insufficient funds
    When I create a payment with insufficient funds
    Then the response status code should be 201
    And the payment status should be "INSUFFICIENT_FUNDS"

  @negative
  Scenario: Payment declined due to invalid CVV
    When I create a payment with invalid CVV
    Then the response status code should be 201
    And the payment status should be "INVALID_SECURITY_CODE"

  @negative
  Scenario: Create payment with missing account_id
    When I create a payment without account id
    Then the response status code should be 400

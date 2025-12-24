Feature: Authorization Payment (Two-Step)

  @sanity @integration
  Scenario: Create authorization successfully
    When I create an authorization payment
    Then the response status code should be 201
    And the payment status should be "AUTHORIZED"

  @negative
  Scenario: Authorization with declined card
    When I create an authorization with insufficient funds
    Then the response status code should be 201
    And the payment status should be "INSUFFICIENT_FUNDS"

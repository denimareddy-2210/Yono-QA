Feature: Verify Payment

  @sanity @integration
  Scenario: Verify valid card
    When I verify a card payment
    Then the response status code should be 201

  @negative
  Scenario: Verify invalid card
    When I verify a card payment with invalid card
    Then the response status code should be 201
    And the payment status should be "INVALID_CARD_DATA"

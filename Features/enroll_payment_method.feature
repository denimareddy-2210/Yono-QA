Feature: Enroll Payment Method

  @sanity @integration
  Scenario: Enroll card payment method for customer
    Given a customer exists
    When I enroll a card payment method for the customer
    Then the response status code should be 200

  @regression
  Scenario: Enroll same card again
    Given a customer exists
    And a card is already enrolled
    When I enroll the same card again
    Then the old card should be unenrolled

  @negative
  Scenario: Enroll payment method with invalid customer id
    When I enroll a payment method with invalid customer id
    Then the response status code should be 400

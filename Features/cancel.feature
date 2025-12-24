Feature: Cancel Payment

  @sanity @integration
  Scenario: Cancel authorized payment
    Given an authorized payment exists
    When I cancel the authorized payment
    Then the response status code should be 200

  @negative
  Scenario: Cancel with invalid transaction id
    Given an authorized payment exists
    When I cancel payment with invalid transaction id
    Then the response status code should be 400

  @negative
  Scenario: Cancel already captured payment
    Given a captured payment exists
    When I cancel the authorized payment
    Then the response status code should be 400

Feature: Capture Authorized Payment

  @sanity @integration
  Scenario: Full capture of authorized payment
    Given an authorized payment exists
    When I capture the authorized payment
    Then the response status code should be 200

  @regression @integration
  Scenario: Partial capture of authorized payment
    Given an authorized payment exists
    When I partially capture the authorized payment
    Then the response status code should be 200

  @negative
  Scenario: Capture with invalid transaction id
    Given an authorized payment exists
    When I capture payment with invalid transaction id
    Then the response status code should be 400

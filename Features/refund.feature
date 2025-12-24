Feature: Refund Payment

  @sanity @integration
  Scenario: Full refund of captured payment
    Given a captured payment exists
    When I create a full refund
    Then the response status code should be 200

  @regression @integration
  Scenario: Partial refund of captured payment
    Given a captured payment exists
    When I create a partial refund
    Then the response status code should be 200

  @negative
  Scenario: Refund with invalid transaction id
    Given a captured payment exists
    When I create a refund with invalid transaction id
    Then the response status code should be 400

  @negative
  Scenario: Refund already refunded payment
    Given a refunded payment exists
    When I create a full refund
    Then the response status code should be 400

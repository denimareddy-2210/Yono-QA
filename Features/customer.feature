Feature: Create Customer

  @sanity @integration
  Scenario: Create customer with minimal data
    When I create a customer with minimal data
    Then the response status code should be 201

  @regression @integration
  Scenario: Create customer with full data
    When I create a customer with full data
    Then the response status code should be 201

  @negative
  Scenario: Create customer without merchant customer id
    When I create a customer with missing mandatory fields
    Then the response status code should be 400

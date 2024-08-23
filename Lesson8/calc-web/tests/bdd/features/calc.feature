Feature: Calc

  Background:
    Given we have application running

  Scenario: Login and calc sum of numbers
    When login as "admin" with password "123"
    And request calc operand 1:"1", operand 2:"2", operation:"+"
    Then status must be "success"
    And calc data contains "3"
    And calc message is empty

  Scenario: Login and calc sum empty operands
    When login as "admin" with password "123"
    And request calc operand 1:" ", operand 2:" ", operation:"+"
    Then calc data is empty
    And status must be "error"
    And calc message contains "Unknown error: invalid literal for int() with base 10: ' '"

  Scenario: Login and calc same operand subtraction
    When login as "admin" with password "123"
    And request calc operand 1:"1", operand 2:"1", operation:"-"
    Then calc data contains "0"
    And status must be "success"
    And calc message is empty

  Scenario: Login and calc adding the same operands
    When login as "admin" with password "123"
    And request calc operand 1:"44", operand 2:"44", operation:"+"
    Then calc data contains "88"
    And status must be "success"
    And calc message is empty

  Scenario: Login and calc adding the same operands
    When login as "admin" with password "123"
    And request calc operand 1:"1", operand 2:"2", operation:"*"
    Then calc data is empty
    And status must be "fail"
    And calc message contains "unknown operation"

  Scenario: Calc sum numbers with registered token
    Given we have registered token "2b62-84fb" for user "test"
    When request calc operand 1:"1", operand 2:"2", operation:"+"
    Then calc data contains "3"
    And status must be "success"
    And calc message is empty

  Scenario: Calc sum numbers with not registered token
    Given we have registered token "29f0c771-cd0b-4f0b-9f72-dce04c2acb0f" for user "frost"
    When We used an unregistered token "d8f7ff73-ab3c-432b-a382"
    And request calc operand 1:"1", operand 2:"2", operation:"+"
    Then calc data is empty
    And status must be "fail"
    And calc message contains "invalid token"


Feature: Login

  Background:
    Given we have application running

  Scenario: Login as valid user
    When login as "admin" with password "123"
    Then status must be "success"
    And token must have value


  Scenario: Login as valid second user
    When login as "john" with password "qwerty"
    Then status must be "success"
    And token must have value

  Scenario: Login as invalid user
    When login as "admin1" with password "qwerty"
    Then status must be "fail"
    And token must not have value

  Scenario: Login without password
    When login as "admin" with password " "
    Then status must be "fail"
    And token must not have value

  Scenario: Login without username
    When login as " " with password "123"
    Then status must be "fail"
    And token must not have value

  Scenario: Login without data
    When login as " " with password " "
    Then status must be "fail"
    And token must not have value
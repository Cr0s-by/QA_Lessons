Feature: Login

  Background:
    Given we have application running

  @login_as_valid
  Scenario: Login as valid user
    When login as "admin" with password "123"
    Then status must be "success"
    And token must have value

  Scenario: Login with wrong password
    When login as "admin" with password "wrong_password"
    Then status must be "fail"
    And token must not have value

  Scenario: Login as not registered user
    When login as "not_registered" with password "123"
    Then status must be "fail"
    And token must not have value
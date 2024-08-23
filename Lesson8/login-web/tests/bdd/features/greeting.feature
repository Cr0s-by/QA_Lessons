Feature: Greeting

  Background:
    Given we have application running

  @login_as_valid
  Scenario: Get greeting as valid user
    When login as "admin" with password "123"
    And request greeting
    Then greeting message contains "admin"

  Scenario: Get greeting with valid token
    Given we have registered token "123456" for user "anton"
    When request greeting
    Then greeting message contains "anton"

  Scenario: Get greeting without authentication
    When request greeting
    Then greeting message is empty
    And status must be "fail"
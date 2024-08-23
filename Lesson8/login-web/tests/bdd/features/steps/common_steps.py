from behave import given, then

from app import application
from configuration import TestConfig


@given('we have application running')
def start_app(context):
    application.config.from_object(TestConfig)
    context.client = application.test_client()


@then('status must be "{value}"')
def assert_response_status(context, value):
    assert value == context.response_status

from behave import given, when, then
import json

from app.services.AuthService import AuthService


@given('we have registered token "{token}" for user "{user_name}"')
def register_token(context, token, user_name):
    AuthService.add_token(token, user_name)
    context.auth_token = token


@when('request greeting')
def greeting(context):
    headers = {}
    if 'auth_token' in context:
        headers['x-auth-token'] = context.auth_token

    response = context.client.get('/greeting', headers=headers)
    assert 200 == response.status_code

    response_data = json.loads(response.get_data())
    context.greeting_message = response_data['data']
    context.response_status = response_data['status']


@then('greeting message contains "{value}"')
def assert_username_in_greeting_message(context, value):
    assert value in context.greeting_message


@then('greeting message is empty')
def assert_greeting_message_is_empty(context):
    assert context.greeting_message is None

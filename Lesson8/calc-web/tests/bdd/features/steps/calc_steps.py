from behave import given, when, then
import json
from app.services.AuthService import AuthService


@given('we have registered token "{token}" for user "{user_name}"')
def register_token(context, token, user_name):
    AuthService.add_token(token, user_name)
    context.auth_token = token


@when('We used an unregistered token "{token}"')
def register_token(context, token):
    context.auth_token = token


@when('request calc operand 1:"{op1}", operand 2:"{op2}", operation:"{operation}"')
def calc(context, op1, op2, operation):
    calc_data = {
        "op1": op1,
        "op2": op2,
        "operation": operation
    }

    headers = {}
    if 'auth_token' in context:
        headers['x-auth-token'] = context.auth_token

    calc_response = context.client.post('/calc', data=json.dumps(calc_data), content_type='application/json',
                                        headers=headers)

    calc_response_data = json.loads(calc_response.get_data())
    context.response_status = calc_response_data['status']
    context.calc_message = calc_response_data["message"]
    context.calc_data = calc_response_data['data']


@then('calc message contains "{value}"')
def assert_username_in_calc_message(context, value):
    assert value in json.dumps(context.calc_message)


@then('calc message is empty')
def assert_calc_message_is_empty(context):
    assert context.calc_message is None


@then('calc data contains "{value}"')
def assert_username_in_calc_data(context, value):
    assert value in json.dumps(context.calc_data)


@then('calc data is empty')
def assert_calc_data_is_empty(context):
    assert context.calc_data is None

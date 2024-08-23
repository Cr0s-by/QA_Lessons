from behave import when, then
import json


@when('login as "{user_name}" with password "{password}"')
def log_in(context, user_name, password):
    login_data = {
        'userName': user_name,
        'password': password
    }

    response = context.client.post('/login', data=json.dumps(login_data), content_type='application/json')
    assert 200 == response.status_code

    response_data = json.loads(response.get_data())
    context.response_status = response_data['status']
    if ((response_data['data'] is not None)
            and ('token' in response_data['data'])):
        context.auth_token = response_data['data']['token']


@then('token must have value')
def assert_token_exist(context):
    assert 'auth_token' in context and context.auth_token is not None


@then('token must not have value')
def assert_token_not_exist(context):
    assert 'auth_token' not in context or context.auth_token is None

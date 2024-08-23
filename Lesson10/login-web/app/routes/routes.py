from flask import render_template, request

from app import application
from app.routes.support import api
from app.services.AuthService import AuthService
from app.services.GreetingService import GreetingService


@application.route('/', methods=['GET'])
def site():
    return render_template('index.html')


@application.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    auth = AuthService()

    authResult = auth.login(data)

    if authResult.success:
        return api.success(authResult)

    return api.fail(None, 'fail')


@application.route('/greeting', methods=['GET'])
def greeting():
    token = request.headers.get('x-auth-token')

    if token is None:
        return api.fail(None, 'anauthorized')

    auth = AuthService()

    if not auth.verify_token(token):
        return api.fail(None, 'invalid token')

    userName = AuthService.get_user_name(token)

    greeting_service = GreetingService()

    return api.success(greeting_service.get(userName))

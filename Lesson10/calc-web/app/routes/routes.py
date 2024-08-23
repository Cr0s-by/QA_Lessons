from flask import render_template, request

from app import application
from app.routes.support import api
from app.services.AuthService import AuthService
from app.services.MathService import MathService

tmp = 1

@application.route('/', methods=['GET'])
def site():
    global tmp

    tmp += 1

    #return api.success(tmp)

    return render_template('index.html')


@application.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    auth = AuthService()

    authResult = auth.login(data)

    if authResult.success:
        return api.success(authResult)

    return api.fail(None, 'fail')


@application.route('/calc', methods=['POST'])
def calc():
    token = request.headers.get('x-auth-token')

    if token is None:
        return api.fail(None, 'anauthorized')

    auth = AuthService()

    if not auth.verify_token(token):
        return api.fail(None, 'invalid token')

    data = request.get_json()

    math_service = MathService()

    op1 = int(data['op1'])
    op2 = int(data['op2'])

    operation = data['operation']

    if operation == '+':
        return api.success(math_service.sum(op1, op2))

    if operation == '-':
        return api.success(math_service.sub(op1, op2))

    return api.fail(None, 'unknown operation')

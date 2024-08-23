import jsonpickle

from app import application


class ApiStatus:
    SUCCESS = 'success'
    FAIL = 'fail'
    ERROR = 'error'


class ApiResponse:
    def __init__(self, *, status=ApiStatus.SUCCESS, data=None, message=None):
        self.message = message
        self.data = data
        self.status = status


def success(data):
    return jsonpickle.encode(ApiResponse(status=ApiStatus.SUCCESS, data=data), unpicklable=False)


def fail(data, message):
    return jsonpickle.encode(ApiResponse(status=ApiStatus.FAIL, data=data, message=message), unpicklable=False)


def validation_failed(data, message='Validation error(s)'):
    response = {
        '_form': data
    }
    return jsonpickle.encode(ApiResponse(status=ApiStatus.FAIL, data=response, message=message), unpicklable=False)


@application.errorhandler(404)
def not_found(e):
    return jsonpickle.encode(ApiResponse(status=ApiStatus.ERROR, message=e.description), unpicklable=False), 404


@application.errorhandler(400)
def bad_request(e):
    return jsonpickle.encode(ApiResponse(status=ApiStatus.FAIL, message=e.description), unpicklable=False), 400


@application.errorhandler(Exception)
def unknown_error(e):
    return jsonpickle.encode(ApiResponse(status=ApiStatus.ERROR, message='Unknown error: ' + str(e)),
                             unpicklable=False), 500

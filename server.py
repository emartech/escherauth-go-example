from flask import Flask, request, Response
from escherauth_go.escher_validator import EscherValidator, EscherValidatorError
from http import HTTPStatus
from urllib.parse import urlparse
import json


app = Flask(__name__)


validator = EscherValidator('eu/suite/ems_request',
                            [{'keyId':'EscherExample', 'secret':'TheBeginningOfABeautifulFriendship', 'acceptOnly':0}],
                            authHeaderName='X-Ems-Auth',
                            dateHeaderName='X-Ems-Date')

@app.route('/')
def index():
    return 'Server Works!'


@app.route('/validate_request', methods=['GET', 'POST'])
def ok():
    try:
        escher_validate(request)
        print('Request {}'.format(json.dumps(json.loads(request.data))))
        return Response('{}'.format(json.dumps(json.loads(request.data))))
    except EscherValidatorError as e:
        return Response('Authorization required {}'.format(e), HTTPStatus.UNAUTHORIZED)





def escher_validate(web_request):
    parsed_url = urlparse(web_request.url)
    url = (parsed_url.path + '?' + parsed_url.query).rstrip('?')
    validator.validateRequest(
        web_request.method,
        url,
        web_request.data.decode('utf-8'),
        web_request.headers
    )


from escherauth_go.escher_signer import EscherSigner, EscherSignerError

import requests


signer = EscherSigner('EscherExample', 'TheBeginningOfABeautifulFriendship', 'eu/suite/ems_request')

def sign_and_send(body, url = 'http://docker.for.mac.localhost:5001/validate_request'):
    try:
        signed_headers = signer.signRequest(
            'POST',
            '/validate_request',
            body,
            {
                'host': 'localhost:5000'
            })
        signed_headers.update({'Content-Type':'application/json'})
        return requests.post(url, data=body, headers= signed_headers)
    except EscherSignerError as e:
        # Handle sign error
        print(e)



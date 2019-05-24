Code examples for EscherPython - HTTP request signing lib
=========================================================

1. Install gems with: `pip install escherauth-go`
2. sign a request: `client.py`
3. Flask server uses escher validation `server.py`

Code examples for the Escher HTTP request signing library (https://github.com/emartech/escher-python).

Build image

    docker build

Start docker

    docker run -it --rm --name flaskapp  -v ${PWD}:/srv/flask_app -e FLASK_APP=server.py -e FLASK_ENV=development -p 5000:5000 flaskapp
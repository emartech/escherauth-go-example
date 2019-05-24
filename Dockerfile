FROM python:3.7-slim
COPY . /srv/flask_app
WORKDIR /srv/flask_app
RUN apt-get clean \
    && apt-get -y update
RUN pip install --requirement requirements.txt
EXPOSE 5000
EXPOSE 5001
CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0" ]


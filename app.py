import os

from flask import Flask, request

app = Flask(__name__)
APP_PATH = os.environ.get('APP_PATH', '')


def route(url, *args, **kwargs):
    url = APP_PATH + url
    return app.route(url, *args, **kwargs)


@route('/oauth-redirect/')
def oauth_redirect():
    return 'ok'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

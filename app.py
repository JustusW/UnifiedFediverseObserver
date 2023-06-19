import os
import signal
from pprint import pprint

import webview
from flask import Flask, render_template
from requests import request as rq


app = Flask(__name__)


class Requester:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def load(self, fragment):
        try:
            localReturn = rq("GET", '%s' % (self.endpoint),
                             headers={"Accept": "application/activity+json"})
        except Exception as e:
            print(e)
            return None

        data = localReturn.json()
        try:
            pprint(data)
        except Exception as e:
            print(e)
        return data


class JSApi:
    def __init__(self):
        self.target = ""

    def abort(self):
        os.kill(os.getpid(), signal.SIGINT)

    def load(self):
        r = Requester(self.target)
        data = r.load("")
        app.app_context().push()
        data["toplevel"] = True
        return render_template('entity.jinja2', data=data)

    def search(self, searchString):
        self.target = searchString


@app.route('/')
def hello_world():
    return render_template('index.jinja2')


api = JSApi()
webview.create_window('UFO', app, js_api=api)
webview.start(debug=True)

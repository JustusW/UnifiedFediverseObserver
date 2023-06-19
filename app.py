import os
import signal
from pprint import pprint

import webview
from flask import Flask, render_template
from requests import request as rq

from models.search_result import SearchResult

app = Flask(__name__)


class Requester:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def load(self):
        try:
            localReturn = rq("GET", '%s' % self.endpoint,
                             headers={"Accept": "application/activity+json"})
        except Exception as e:
            print(e)
            return None

        data = localReturn.json()
        return SearchResult(data, app)


class JSApi:
    def __init__(self):
        self.target = ""

    def abort(self):
        os.kill(os.getpid(), signal.SIGINT)

    def load(self):
        try:
            r = Requester(self.target)
            app.app_context().push()
            return str(r.load())
        except Exception as e:
            raise e
            # return {"failure": str(e)}

    def search(self, searchString):
        self.target = searchString


@app.route('/')
def hello_world():
    return render_template('index.jinja2')


api = JSApi()
webview.create_window('UFO', app, js_api=api)
webview.start(debug=True)

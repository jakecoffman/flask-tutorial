import flask, flask.views
import os

class Main(flask.views.MethodView):
    def get(self, page="index"):
        page += ".html"
        if os.path.isfile('templates/' + page):
            return flask.render_template(page)
        flask.abort(404)

# Estava dando um erro em flask.helpers em um modelo chamado pela função 5 linhas abaixo, as proximas 3 são uma armação de macaco pra resolver
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
import flask_restful

import werkzeug
from werkzeug.utils import cached_property
werkzeug.cached_property = cached_property
from flask import Flask
from flask_restplus import Api

"""
    Função para criar instancia da Api
"""

class Server():
    """description of class"""

    def __init__(self, ):
        self.app = Flask(__name__)
        self.api = Api(self.app,
                       version="1.0",
                       title="Simple Test Api",
                       description="Simple Test Api",
                       doc="/docs"
            )
    def run(self,):
        self.app.run(
            debug=True
            )

server = Server()
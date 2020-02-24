from flask_restplus import Resource
from flask import request, jsonify
from zen.api import api
from zen.api.quotes import Quotes

import logging
import json


log = logging.getLogger(__name__)

ns = api.namespace(
    '/', description='List Zen Quotes')

@ns.route('/')
@ns.route('/<string:lang>')
class List(Resource):
    @ns.response(code=400, description="Bad Request")
    def get(self, lang=None):
        """
        Lista todos as citações do Zen do Python em pt ou en.
        """
        q = Quotes()
        res = q.get_quotes(lang)

        return res
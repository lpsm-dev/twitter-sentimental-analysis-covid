# -*- coding: utf-8 -*-

from restplus import api
from flask_restplus import fields

tweets_serializer = api.model(
  "Tweets",
  {
    "text": fields.String(required=True),
    "count": fields.Integer(required=False),
    "result_type": fields.String(required=False),
    "language": fields.String(required=True)
  }
)

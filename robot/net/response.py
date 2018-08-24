from flask import Response


class Response(Response):
    charset = 'utf-8'
    default_status = 200


import json

class Response(dict):
    def __init__(self, data, message='Successful operation', status=200):
        dict.__init__(self, data=data, message=message, status=status)
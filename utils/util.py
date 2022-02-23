from flask import jsonify
from utils.Response import *
import json

def get_reponse(data, status = 200):
    response = json.dumps(Response(data, status=status))
    response_dict = json.loads(response)
    response_json = jsonify(response_dict)
    response_json.status_code = status
    return response_json

def get_exception(err: BaseException, status = 400):
    message = str(err.args[0])
    response = json.dumps(Response(None, message=message, status=status))
    response_dict = json.loads(response)
    response_json = jsonify(response_dict)
    response_json.status_code = status
    return response_json
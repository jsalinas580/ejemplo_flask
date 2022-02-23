from flask import request
from models.Suma import suma
from utils.util import get_reponse, get_exception


def suma_controler():
    try:
        request_json = request.get_json()
        entradas = dict(request_json)
        a = float(entradas['a'])
        b = float(entradas['b'])
        result = suma(a, b)
        return get_reponse(result)
    except BaseException as err:
        return get_exception(err)

from flask import make_response
import json
from flask_api import status


# serializes assuming data is a collection
def successful_collection_response(data):
    data = list(map(lambda x: x.serialize(), data))
    return _response(data)


# serializes assuming data is NOT a collection
def successful_object_response(data):
    if data is None:
        data = None
        return _response(data)
    else:
        data = data.serialize()
        return _response(data)


# does not serialize
def successful_text_response(data):
    return _response(data)


def not_found_error_response(data):
    return _response(data, status.HTTP_404_NOT_FOUND)


def bad_request_error_response(data):
    return _response(data, status.HTTP_400_BAD_REQUEST)


def _response(data, status_code=status.HTTP_200_OK):
    if data is None:
        response = make_response('', 204)
        response.mimetype = 'application/json'
        return response
    else:
        response = make_response(json.dumps(data), status_code)
        response.mimetype = 'application/json'
        return response


def successful_object_response_for_external_api(data):
    if data is None:
        data = None
        return _response(data)
    else:
        data = data.serialize_external()
        return _response(data)






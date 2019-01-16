import requests
import json
from .store import storage

# defines some parts of the header, to combine together
header_parts = {
    'common': {'mode': 'cors'},
    'json': {'Content-Type': 'application/json'},
    'text': {'sendAs': 'text', 'Content-Type': 'text/plain'}
}
default_type = 'json'
header_parts['default'] = header_parts[default_type]


def prepare_header(type='default'):
    """
        Prepare the header of the HTTP request by fetching the token from the config
        and few other things.

        :param type: string. Must be one of the keys in the above declared dict header_parts
    """

    # if posting a file, the request module deals with the content-type
    if type == "file":
        header = {**header_parts['common']}
    else:
        header = {**header_parts['common'], **header_parts[type]}

    if storage.has('token'):
        header['Authorization'] = 'Bearer ' + storage.get('token')
    return header


def prepare_body(data, type='default'):
    """
        Prepare the body of the HTTP request

        :param data:
        :param type:
        :return:
    """
    if type == 'default':
        type = default_type
    body = None

    if type == 'json':
        body = json.dumps(data, ensure_ascii=True)
    else:
        body = data

    if data is None:
        body = None

    return body


def print_request_response(r):
    print('status: ', r.status_code)
    print('encoding: ', r.encoding)
    print('url: ', r.url)
    print('json: ', r.json())
    print('text: ', r.text)
    print('headers: ')
    print(r.headers)
    print('cookies:', r.cookies)
    print('history: ', r.history)


def http_get(path, params=None, use_base=False, get_raw_response=False, stream=False):
    """
        Wrapper to perform a GET request.

        :param path: complete URL if use_base si False or just the ending if use_base is True
        :param params: OPTIONAL provide some URL parameters (?foo=bar&hello=world) as a dictionary
        :param use_base: OPTIONAL if True, the Nexus env provided by nexus.config.set_environment will
        be prepended to path. (default: False)
        :param get_raw_response: OPTIONAL If True, the object provided by requests.get will be directly returned as is
        (convenient when getting a binary file). If False, a dictionary representation of the response will be returned
        (default: False)
        :param stream: OPTIONAL True if GETting a file (default: False)
        :return: if get_raw_response is True, returns the request.get object. If get_raw_response is False, return the
        dictionary that is equivalent to the json response
    """
    header = prepare_header()
    full_url = (storage.get('environment') if use_base else '') + path
    response = requests.get(full_url, headers=header, stream=stream, params=params)
    response.raise_for_status()

    if get_raw_response:
        return response
    else:
        return json.loads(response.text)


def http_post(path, body=None, data_type='default', params=None):
    """
        Perform a POST request.

        :param path: complete URL if use_base si False or just the ending if use_base is True
        :param body: OPTIONAL Things to send, can be a dictionary
        :param data_type: OPTIONAL can be 'json' or 'text' (default: 'default' = 'json')
        :param params: OPTIONAL provide some URL parameters (?foo=bar&hello=world) as a dictionary
        :return: the dictionary that is equivalent to the json response
    """
    header = prepare_header(data_type)
    full_url = storage.get('environment') + path
    body_data = prepare_body(body, data_type)
    response = requests.post(full_url, headers=header, data=body_data, params=params)
    response.raise_for_status()
    return json.loads(response.text)


def http_put(path, body=None, data_type='default', use_base=False, params=None):
    """
        Performs a PUT request

        :param path: complete URL if use_base si False or just the ending if use_base is True
        :param body: OPTIONAL Things to send, can be a dictionary or a buffer
        :param data_type: OPTIONAL can be 'json' or 'text'or 'file' (default: 'default' = 'json')
        :param use_base: OPTIONAL if True, the Nexus env provided by nexus.config.set_environment will
        be prepended to path. (default: False)
        :param params: OPTIONAL provide some URL parameters (?foo=bar&hello=world) as a dictionary
        :return: the dictionary that is equivalent to the json response
    """
    header = prepare_header(data_type)
    full_url = (storage.get('environment') if use_base else '') + path
    response = None

    if data_type != 'file':
        body_data = prepare_body(body, data_type)
        response = requests.put(full_url, headers=header, data=body_data, params=params)
    else:
        response = requests.put(full_url, headers=header, files=body, params=params)

    response.raise_for_status()
    return json.loads(response.text)


def http_patch(path, body=None, data_type='default', use_base=False, params=None):
    """
        Performs a PATCH request

        :param path: complete URL if use_base si False or just the ending if use_base is True
        :param body: OPTIONAL Things to send, can be a dictionary
        :param data_type: OPTIONAL can be 'json' or 'text' (default: 'default' = 'json')
        :param params: OPTIONAL provide some URL parameters (?foo=bar&hello=world) as a dictionary
        :param use_base: OPTIONAL if True, the Nexus env provided by nexus.config.set_environment will
        be prepended to path. (default: False)
        :return: the dictionary that is equivalent to the json response
    """
    header = prepare_header()
    full_url = (storage.get('environment') if use_base else '') + path
    body_data = prepare_body(body, data_type)
    response = requests.patch(full_url, headers=header, data=body_data, params=params)
    return response


def http_delete(path, body=None, data_type='default', use_base=False, params=None):
    """
        Performs a DELETE request

        :param path: complete URL if use_base si False or just the ending if use_base is True
        :param body: OPTIONAL Things to send, can be a dictionary
        :param data_type: OPTIONAL can be 'json' or 'text' (default: 'default' = 'json')
        :param params: OPTIONAL provide some URL parameters (?foo=bar&hello=world) as a dictionary
        :param use_base: OPTIONAL if True, the Nexus env provided by nexus.config.set_environment will
        be prepended to path. (default: False)
        :return: the dictionary that is equivalent to the json response
    """
    header = prepare_header()
    full_url = (storage.get('environment') if use_base else '') + path
    body_data = prepare_body(body, data_type)
    response = requests.delete(full_url, headers=header, data=body_data, params=params)
    response.raise_for_status()
    return json.loads(response.text)


def is_response_valid(response):
    """
        Not really used anymore. Says if the answer to a request is valid or not.

        :param response: object returned by requests.get/put/post/delete/patch
        :return: True if status is below 300, False if above
    """
    return response.status_code < 300
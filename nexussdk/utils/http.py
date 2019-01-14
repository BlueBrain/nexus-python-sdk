import requests
import json
from . store import storage

# defines some parts of the header, to combine together
header_parts = {
    'common': {'mode': 'cors'},
    'json': {'Content-Type': 'application/json'},
    'file': {'Content-Type': 'application/octet-stream'}, # not used
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


def http_get(path, use_base = True):
    header = prepare_header()
    full_url = (storage.get('environment') if use_base else '') + path
    response = requests.get(full_url, headers=header)
    response.raise_for_status()
    return json.loads(response.text)


def http_post(path, body=None, data_type='default'):
    header = prepare_header(data_type)
    full_url = storage.get('environment') + path
    body_data = prepare_body(body, data_type)
    response = requests.post(full_url, headers=header, data=body_data)
    response.raise_for_status()
    return json.loads(response.text)


# def http_put(path, body=None, data_type='default', use_base = True):
#     header = prepare_header()
#     full_url = (storage.get('environment') if use_base else '') + path
#     body_data = prepare_body(body, data_type)
#     response = requests.put(full_url, headers=header, data=body_data)
#     response.raise_for_status()
#     return json.loads(response.text)


def http_put(path, body=None, data_type='default', use_base = True):
    header = prepare_header(data_type)
    full_url = (storage.get('environment') if use_base else '') + path

    response = None

    if data_type != 'file':
        body_data = prepare_body(body, data_type)
        response = requests.put(full_url, headers=header, data=body_data)
    else:

        response = requests.put(full_url, headers=header, files=body)

    response.raise_for_status()
    return json.loads(response.text)


def http_delete(path, body=None, data_type='default', use_base = True):
    header = prepare_header()
    full_url = (storage.get('environment') if use_base else '') + path
    body_data = prepare_body(body, data_type)
    response = requests.delete(full_url, headers=header, data=body_data)
    response.raise_for_status()
    return json.loads(response.text)


def is_response_valid(response):
    return response.status_code < 300

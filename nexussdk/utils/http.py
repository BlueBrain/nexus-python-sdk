import requests
import json
from . store import storage

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
    type: string. Must be one of the keys in the above declared dict header_parts
    """
    header = {**header_parts['common'], **header_parts[type]}
    if storage.has('token'):
        header['Authorization'] = 'Bearer ' + storage.get('token')
    return header


def prepare_body(data, type='default'):
    if type == 'default':
        type = default_type
    body = None

    if type == 'json':
        body = json.dumps(data, ensure_ascii=True)
    elif type == 'text':
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


def http_get(url, use_base = True):
    header = prepare_header()
    full_url = (storage.get('environment') if use_base else '') + url
    response = requests.get(full_url, headers=header)
    return response


def http_post(url, body=None, data_type='default'):
    header = prepare_header(data_type)
    full_url = storage.get('environment') + url
    body_data = prepare_body(body, data_type)
    response = requests.post(full_url, headers=header, data=body_data)
    return response


def http_put(url, body=None, data_type='default', use_base = True):
    header = prepare_header()
    full_url = (storage.get('environment') if use_base else '') + url
    body_data = prepare_body(body, data_type)
    response = requests.put(full_url, headers=header, data=body_data)
    return response


def http_patch(url, body=None, data_type='default', use_base=True):
    header = prepare_header()
    full_url = (storage.get('environment') if use_base else '') + url
    body_data = prepare_body(body, data_type)
    response = requests.patch(full_url, headers=header, data=body_data)
    return response


def http_delete(url, body=None, data_type='default', use_base = True):
    header = prepare_header()
    full_url = (storage.get('environment') if use_base else '') + url
    body_data = prepare_body(body, data_type)
    response = requests.delete(full_url, headers=header, data=body_data)
    return response


def is_response_valid(response):
    return (response.status_code < 300)

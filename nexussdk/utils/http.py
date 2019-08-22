import collections
import json
from typing import List, Union, Optional

import requests
from sseclient import SSEClient


class Http:
    default_type = "json"

    # defines some parts of the header, to combine together
    header_parts = {
        "common": {"mode": "cors"},
        "json": {"Content-Type": "application/json"},
        "text": {"sendAs": "text", "Content-Type": "text/plain"},
        "sparql": {"Content-Type": "application/sparql-query"},
        "file": {},
    }

    # so that a get request can decide to retrieve JSON or binary
    header_accept = {
        "json": "application/ld+json, application/json",
        "all": "*/*"
    }

    def __init__(self, environment: str, token: Optional[str] = None):
        self.env = environment
        self.token = token

    def get(this, path: Union[str, List[str]], stream=False, get_raw_response=False, use_base=False,
            data_type=default_type, accept="json", **kwargs):
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
        header = this._prepare_header(data_type, accept)
        full_url = this._full_url(path, use_base)
        params = kwargs.pop("params", None)
        if params:
            response = requests.get(full_url, headers=header, stream=stream, params=params, **kwargs)
        else:
            response = requests.get(full_url, headers=header, stream=stream, params=kwargs)
        response.raise_for_status()

        if get_raw_response:
            return response
        else:
            return this._decode_json_ordered(response.text)

    def post(self, path: Union[str, List[str]], body=None, data_type=default_type, use_base=False, **kwargs):
        """
            Perform a POST request.

            :param path: complete URL if use_base si False or just the ending if use_base is True
            :param body: OPTIONAL Things to send, can be a dictionary
            :param data_type: OPTIONAL can be "json" or "text" (default: "default" = "json")
            :param params: OPTIONAL provide some URL parameters (?foo=bar&hello=world) as a dictionary
            :return: the dictionary that is equivalent to the json response
        """
        header = self._prepare_header(type=data_type)
        full_url = self._full_url(path, use_base)

        # body_data = prepare_body(body, data_type)
        # response = requests.post(full_url, headers=header, data=body_data, params=kwargs)

        response = None

        if data_type != "file":
            body_data = self._prepare_body(body, data_type)
            response = requests.post(full_url, headers=header, data=body_data, params=kwargs)
        else:
            response = requests.post(full_url, headers=header, files=body, params=kwargs)

        response.raise_for_status()
        return self._decode_json_ordered(response.text)

    def put(self, path: Union[str, List[str]], body=None, data_type=default_type, use_base=False, **kwargs):
        """
            Performs a PUT request

            :param path: complete URL if use_base si False or just the ending if use_base is True
            :param body: OPTIONAL Things to send, can be a dictionary or a buffer
            :param data_type: OPTIONAL can be "json" or "text" or "file" (default: "default" = "json")
            :param use_base: OPTIONAL if True, the Nexus env provided by nexus.config.set_environment will
            be prepended to path. (default: False)

            :param params: OPTIONAL provide some URL parameters (?foo=bar&hello=world) as a dictionary
            :return: the dictionary that is equivalent to the json response
        """
        header = self._prepare_header(type=data_type)
        full_url = self._full_url(path, use_base)
        response = None

        if data_type != "file":
            body_data = self._prepare_body(body, data_type)
            response = requests.put(full_url, headers=header, data=body_data, params=kwargs)
        else:
            response = requests.put(full_url, headers=header, files=body, params=kwargs)

        response.raise_for_status()
        return self._decode_json_ordered(response.text)

    def patch(self, path: Union[str, List[str]], body=None, data_type=default_type, use_base=False, **kwargs):
        """
            Performs a PATCH request

            :param path: complete URL if use_base si False or just the ending if use_base is True
            :param body: OPTIONAL Things to send, can be a dictionary
            :param data_type: OPTIONAL can be "json" or "text" (default: "default" = "json")
            :param params: OPTIONAL provide some URL parameters (?foo=bar&hello=world) as a dictionary
            :param use_base: OPTIONAL if True, the Nexus env provided by nexus.config.set_environment will
            be prepended to path. (default: False)
            :return: the dictionary that is equivalent to the json response
        """
        header = self._prepare_header()
        full_url = self._full_url(path, use_base)
        body_data = self._prepare_body(body, data_type)
        response = requests.patch(full_url, headers=header, data=body_data, params=kwargs)
        response.raise_for_status()
        return self._decode_json_ordered(response.text)

    def delete(self, path: Union[str, List[str]], body=None, data_type=default_type, use_base=False, **kwargs):
        """
            Performs a DELETE request

            :param path: complete URL if use_base si False or just the ending if use_base is True
            :param body: OPTIONAL Things to send, can be a dictionary
            :param data_type: OPTIONAL can be "json" or "text" (default: "default" = "json")
            :param params: OPTIONAL provide some URL parameters (?foo=bar&hello=world) as a dictionary
            :param use_base: OPTIONAL if True, the Nexus env provided by nexus.config.set_environment will
            be prepended to path. (default: False)
            :return: the dictionary that is equivalent to the json response
        """
        header = self._prepare_header()
        full_url = self._full_url(path, use_base)
        body_data = self._prepare_body(body, data_type)
        response = requests.delete(full_url, headers=header, data=body_data, params=kwargs)
        response.raise_for_status()
        return self._decode_json_ordered(response.text)

    def sse_request(self, path: str, last_id: Optional[str], ):
        """
            Performs a GET requests to an SSE endpoint.

            :param path: path of the request
            :param last_id: ID of the last processed event, if provided, only events after
                    the event with the provided ID will be returned.
            :return: iterator of SSE events
        """
        return SSEClient(self._full_url(path, True), last_id, headers=self._prepare_header())

    # Internal helpers
    def _full_url(self, path: Union[str, List[str]], use_base: bool) -> str:
        # 'use_base' is temporary for compatibility with previous code sections.
        if use_base:
            return self.env + path

        if isinstance(path, str):
            return path
        elif isinstance(path, list):
            url = [self.env] + path
            return "/".join(url)
        else:
            raise TypeError("Expecting a string or a list!")

    def _prepare_header(self, type=default_type, accept="json"):
        """
            Prepare the header of the HTTP request by fetching the token from the config
            and few other things.

            :param type: string. Must be one of the keys in the above declared dict header_parts
            :param accept: OPTIONAL if "json", the answer will be JSON, if "all" it will be something else if the
                           request can send something else (e.g. binary)

        """

        header = {**Http.header_parts["common"], **Http.header_parts[type]}

        if accept in Http.header_accept:
            header["Accept"] = Http.header_accept[accept]

        if self.token:
            header["Authorization"] = "Bearer " + self.token
        return header

    def _prepare_body(self, data, type=default_type):
        """
            Prepare the body of the HTTP request

            :param data:
            :param type:
            :return:
        """
        body = None

        if type == "json":
            body = json.dumps(data, ensure_ascii=True)
        else:
            body = data

        if data is None:
            body = None

        return body

    # to make sure the output response dictionary are always ordered like the response's json
    def _decode_json_ordered(self, s: str):
        return json.JSONDecoder(object_pairs_hook=collections.OrderedDict).decode(s)

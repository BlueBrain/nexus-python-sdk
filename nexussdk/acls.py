import json
from typing import Dict

from utils.http import (http_delete, http_get, http_patch, http_put)


def output(with_pretty_print=True):
    def decorator(func):
        def wrapper(*args, **kwargs):
            response = func(*args, **kwargs)
            if with_pretty_print:
                print("{} {}".format(response.request.method, response.url))
                print(json.dumps(response.json(), indent=2))
            if not with_pretty_print:
                return response.json()
        return wrapper
    return decorator


# Create functions.

@output()
def create(path: str, acls: Dict) -> Dict:
    # PUT /v1/acls/{subpath}
    return http_put(path, acls, use_base=False)


# Read functions.

@output()
def fetch(path: str, rev: int = None, self: bool = True) -> Dict:
    # GET /v1/acls/{subpath}?rev={rev}&self={self}
    if rev is None:
        url = "{}?self={}".format(path, self)
    else:
        url = "{}?rev={}&self={}".format(path, rev, self)
    return http_get(url, use_base=False)


@output()
def list_(path: str, ancestors: bool = False, self: bool = True) -> Dict:
    # GET /v1/acls/{subpath}?ancestors={ancestors}&self={self}
    url = "{}?ancestors={}&self={}".format(path, ancestors, self)
    return http_get(url, use_base=False)


# Update functions.

@output()
def replace(path: str, rev: int, acls: Dict) -> Dict:
    # PUT /v1/acls/{subpath}?rev={rev}
    url = "{}?rev={}".format(path, rev)
    return http_put(url, acls, use_base=False)


@output()
def append(path: str, rev: int, acls: Dict) -> Dict:
    # PATCH /v1/acls/{subpath}?rev={rev}
    url = "{}?rev={}".format(path, rev)
    return http_patch(url, acls, use_base=False)


@output()
def subtract(path: str, rev: int, acls: Dict) -> Dict:
    # PATCH /v1/acls/{subpath}?rev={rev}
    url = "{}?rev={}".format(path, rev)
    return http_patch(url, acls, use_base=False)


# Delete functions.

@output()
def delete(path: str, rev: int) -> Dict:
    # DELETE /v1/acls/{subpath}?rev={rev}
    url = "{}?rev={}".format(path, rev)
    return http_delete(url, use_base=False)

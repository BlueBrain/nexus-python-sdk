import json
from typing import Dict, Union, List

from nexussdk.utils.http import (http_delete, http_get, http_patch, http_put)


# FIXME Use directly new http module.
# FIXME Remove after first release.
# Returning directly a Dict and exceptions will be handled by the http module.
def output(is_debug=True):
    def decorator(func):
        def wrapper(*args, **kwargs):
            response = func(*args, **kwargs)
            if is_debug:
                print("{} {}".format(response.request.method, response.url))
                print(json.dumps(response.json(), indent=2))
            else:
                return response.json()
        return wrapper
    return decorator


# Create functions.

@output()
def put(path: Union[str, List[str]], data: Dict, **kwargs) -> Dict:
    return http_put(path, data, params=kwargs)


# Read functions.

@output()
def get(path: Union[str, List[str]], **kwargs) -> Dict:
    return http_get(path, params=kwargs)


# Update functions.

@output()
def patch(path: Union[str, List[str]], data: Dict, **kwargs) -> Dict:
    return http_patch(path, data, params=kwargs)


# Delete functions.

@output()
def delete(path: Union[str, List[str]], **kwargs) -> Dict:
    return http_delete(path, params=kwargs)

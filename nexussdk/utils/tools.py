import copy
import json


def copy_this_into_that(this, that, deepcopy=False, force=False):
    """
        Copy the content of a dictionary within another.

        :param this: the dictionary to be copied into that
        :param that: the dictionary to copy this into
        :param deepcopy: shallow copy (aka. by reference) if False, deepcopy if False (default: False)
        :param force: replaces existing fields if True, does not replace when False (default: False)

        This fucntion does not return anything because the object `that` is modified in place.
    """

    if deepcopy:
        this = copy.deepcopy(this)

    for key, value in this.items():
        if key not in that or force:
            that[key] = value


def pretty_print(payload):
    """
    This helper function display a Python dict in a nice way, using the JSON syntax and an indentation of 2.
    :param payload: A Python dict
    """
    print(json.dumps(payload, indent=2))

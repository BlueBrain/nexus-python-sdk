import copy
import json

from typing import Optional


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


def listing_params(pagination_from: Optional[int], pagination_size: Optional[int],
                    deprecated: Optional[bool], type: Optional[str], created_by: Optional[str],
                    updated_by: Optional[str], rev: Optional[int]):
    """Create a dictionary of the parameters configuring listings.

    Some parameter names are using Python reserved ones. They cannot therefore
    be directly passed to ``requests`` as ``kwargs``.

    :param pagination_from: Pagination index to start from.
    :param pagination_size: Number of results to return per page.
    :param deprecated: Deprecation status of the resolvers to keep.
    :param type: Type of the resolvers to keep, given as an IRI.
    :param created_by: Identity ID of the creator of the resolvers
        to keep, given as an IRI.
    :param updated_by: Identity ID of the last identity which has
        updated the resolvers to keep, given as en IRI.
    :param rev: Revision number of the resolvers to keep.
    :return: Dictionary of the parameters configuring listings.
     """
    return {
        "from": pagination_from,
        "size": pagination_size,
        "deprecated": deprecated,
        "type": type,
        "createdBy": created_by,
        "updatedBy": updated_by,
        "rev": rev,
    }

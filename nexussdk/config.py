"""
The config provides an easy way to handle the Nexus environment and token.
"""


from nexussdk.utils.store import storage


def set_token(token):
    """
    Set the token for the Nexus environment.

    :param token: The token is a string given by Nexus or a connected service.
    """
    storage.set("token", token)


def remove_token():
    """
    Remove the token. Then Nexus will no longer be able to perform any operations.
    """
    storage.delete("token")


def set_environment(env):
    """
    Define the base URL of the Nexus environment. This URL should be of the form `https://my-nexus-env.com/v1`
    Note that it should not finish with a slash.

    :param env: The base URL for the environment
    """
    storage.set("environment", env)

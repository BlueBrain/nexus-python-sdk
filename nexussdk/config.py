from nexussdk.utils.store import storage


def set_token(token):
    storage.set("token", token)


def remove_token():
    storage.delete("token")


def set_environment(env):
    storage.set("environment", env)

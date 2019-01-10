# A genericmap is a simple data holder to inherit from.


class GenericMap:
    def __init__(self):
        self._map = {}

    def set(self, key, value):
        self._map[key] = value

    def get(self, key):
        if key in self._map:
            return self._map[key]
        else:
            raise Exception("No value for the key: " + key)

    def delete(self, key):
        del self._map[key]

    def has(self, key):
        return (key in self._map)

    def list(self):
        return list(self._map.keys())

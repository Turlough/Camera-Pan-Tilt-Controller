import json


class JsonLoader(object):
    """
    Class for reading json into an object,
    with properties that can be accessed using dot notation,
    rather than dictionary notation.

    Example, from_string('{"a":"b")') returns an object
    with property a whose value is "b".
    """

    def from_string(self, data):
        """
        Given a json string,
        return an object with the appropriate properties.
        @:param data: A string of json data.
        """
        self.__dict__ = json.loads(data)
        return self

    def from_file(self, filepath):
        """
        Given a json file,
        return an object with the appropriate properties.
        @:param filepath: path to a file containing json data.
        """
        with open(filepath, 'r') as f:
            self.__dict__ = json.load(f)
            return self

from unittest import TestCase
from remote_control.json_loader import JsonLoader

loader = JsonLoader()


class TestJsonLoader(TestCase):
    def test_from_string(self):
        result = loader.from_string('{"test":"tested"}')
        self.assertEqual('tested', result.test)

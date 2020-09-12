from unittest import TestCase
from json_loader import JsonLoader

loader = JsonLoader()


class TestJsonLoader(TestCase):

    def test_from_string(self):
        result = loader.from_string('{"test":"tested"}')
        self.assertEqual('tested', result.test)

    def test_from_file(self):
        result = loader.from_file('../../mqtt_config.json')
        self.assertEqual(1883, result.port)

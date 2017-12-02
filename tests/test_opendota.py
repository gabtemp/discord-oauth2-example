import unittest
from unittest import mock

import buddy.opendota


class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

    def raise_for_status(self):
        pass


class ClientTest(unittest.TestCase):

    @mock.patch('requests.get', return_value=MockResponse([{"match_id": 3586411048}, {"match_id": 3588133048}], 200))
    def test_recent_matches(self, requests_f):
        config = {'opendota': {'url': 'opendota'}}
        client = buddy.opendota.Client(config)

        last_match = client.last_match('player_id')

        requests_f.assert_called_with('opendota/players/player_id/recentMatches')
        self.assertEqual(last_match, {"match_id": 3586411048})

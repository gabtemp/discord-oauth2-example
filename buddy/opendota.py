import requests


class Client:

    def __init__(self, config_file=None):
        self.config = config_file['opendota']
        self.url = self.config['url']

    def last_match(self, player_id):
        suffix = '/players/%s/recentMatches' % player_id
        response = requests.get(self.url + suffix)
        response.raise_for_status()
        return response.json()[0]

import requests

class SampleApi:
    def get(self, url):
        return requests.get(url, timeout=20)

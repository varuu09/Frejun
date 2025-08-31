import pytest
import requests
from utilities.read_properties import Read_properties

class Test_products:
    url = Read_properties.get_url()


    def test_product(self, login):
        #headers = {"Authorization": f"Bearer {login['token']}"}

        api = requests.get(self.url + 'products')
        assert api.status_code == 200
        data = api.json()
        #print(data)
        assert "products" in data

    def test_unlisted_product(self, login):

        api = requests.get(self.url + 'products/99999')
        assert api.status_code == 404
        assert "message" in api.json()


    def test_wrong_search(self, login):

        api = requests.get(self.url + 'products/search?q=abcdefg')
        assert api.status_code == 200
        body = api.json()
        assert body["total"] == 0
        assert body["products"] == []


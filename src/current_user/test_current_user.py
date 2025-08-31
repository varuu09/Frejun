import pytest
import requests
from utilities.read_properties import Read_properties

class Test_current_user:
    url = Read_properties.get_url()
    username = Read_properties.get_username()

    def test_current_user(self, login):

        headers = {"Authorization": f"Bearer {login['token']}"}
        api = requests.get(self.url + 'auth/me', headers = headers)

        assert api.status_code == 200
        body = api.json()
        assert "id" in body
        assert body["username"] == self.username


    def test_user_without_token(self, login):

        api = requests.get(self.url + 'auth/me')
        assert api.status_code == 401
        body = api.json()
        print(body)
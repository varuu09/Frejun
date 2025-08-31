import pytest
import requests
from utilities.read_properties import Read_properties

class Test_Login:
    url = Read_properties.get_url()
    username = Read_properties.get_username()
    password = Read_properties.get_password()

    def test_login(self, login):
        assert login["status_code"] == 200

    def test_login_failed(self):
        api = requests.post(''+self.url+'auth/login',json={"username": "username","password": "password"})
        assert api.status_code == 400
        body = api.json()
        assert "message" in body

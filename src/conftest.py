import pytest
import requests
from utilities.read_properties import Read_properties


url = Read_properties.get_url()
username = Read_properties.get_username()
password = Read_properties.get_password()

@pytest.fixture(scope="session")
def login():
        api = requests.post(url + 'auth/login',
                            json={"username": username, "password": password})
        response = api.json()
        status_code = api.status_code
        header = api.headers
        token = response.get("accessToken")
        return {
                "status_code": status_code,
                "header": header,
                "token": token
        }


import configparser
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(base_dir, '..', 'configuration', 'config.ini')
config_path = os.path.abspath(config_path)

config = configparser.RawConfigParser()
config.read(config_path)

class Read_properties:

    @staticmethod
    def get_username():
        username = config.get("login_creds", "username")
        return username

    @staticmethod
    def get_password():
        password = config.get("login_creds", "password")
        return password

    @staticmethod
    def get_url():
        url = config.get("common_info", "url")
        return url





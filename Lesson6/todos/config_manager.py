import os
import json

from config import Config


class ConfigManager:

    @staticmethod
    def get_config():
        file_name = os.environ.get('CONFIG_FILE', 'config.json')

        full_path = os.path.join('configs', file_name)

        data = ConfigManager.read_content(full_path)

        return ConfigManager.map_config(data)

    @staticmethod
    def read_content(full_path):
        with open(full_path, 'r') as config:
            return json.load(config)

    @staticmethod
    def map_config(data):
        config = Config()

        config.page_url = data['pageUrl']

        return config

import json
import os

config_file_path = os.path.join(os.path.dirname(__file__), "config.json")
config_file_object = open(config_file_path, "r", encoding="utf-8")
config_file = json.load(config_file_object)

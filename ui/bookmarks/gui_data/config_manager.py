"""
config_manager.py
Keyword: gui_data_config

Odczyt i zapis ustawień (motyw, filtry, preferencje) do pliku .ini/.yaml.
Tu - atrapa używająca pliku .ini przez moduł configparser.
"""

import configparser
import os

CONFIG_FILE = "app_config.ini"

def load_config():
    config = configparser.ConfigParser()
    if os.path.exists(CONFIG_FILE):
        config.read(CONFIG_FILE)
    return config

def save_config(config):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        config.write(f)

def get_theme(config):
    return config.get("Display", "theme", fallback="light")

def set_theme(config, theme):
    if "Display" not in config:
        config["Display"] = {}
    config["Display"]["theme"] = theme

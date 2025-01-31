"""
plugin_manager.py
Keyword: net_api_plugins

Ładowanie wtyczek .py z katalogu plugins; każda może modyfikować scrapowanie/GUI.
"""

import importlib
import os

def load_plugins(plugins_dir):
    """
    Przegląda katalog 'plugins_dir' i importuje każdy plik .py jako moduł wtyczki.
    Zwraca listę załadowanych modułów.
    """
    loaded = []
    for filename in os.listdir(plugins_dir):
        if filename.endswith(".py"):
            plugin_name = filename[:-3]
            try:
                module = importlib.import_module(f"plugins.{plugin_name}")
                loaded.append(module)
            except Exception as e:
                print(f"Błąd ładowania pluginu {plugin_name}: {e}")
    return loaded

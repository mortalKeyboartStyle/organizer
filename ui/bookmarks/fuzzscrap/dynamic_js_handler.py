"""
dynamic_js_handler.py
Keyword: fuzzscrap_dynamic_js

Obsługa JavaScript za pomocą PyQt6 QWebEngineView
lub Puppeteer (Pyppeteer). Tu przykład PyQt6:
"""

from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QEventLoop

def fetch_js_rendered_page(url):
    """
    Używa QWebEngineView do załadowania strony i zwraca HTML
    po załadowaniu JS.
    """
    app_view = QWebEngineView()
    loop = QEventLoop()

    def on_load_finished(_ok):
        loop.quit()

    app_view.loadFinished.connect(on_load_finished)
    app_view.load(url)
    loop.exec()

    # Pobieramy HTML
    page = app_view.page()
    html = ""
    def handle_html(data):
        nonlocal html
        html = data
        loop.quit()

    page.toHtml(handle_html)
    loop.exec()
    return html

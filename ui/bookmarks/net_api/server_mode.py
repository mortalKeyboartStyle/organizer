"""
server_mode.py
Keyword: net_api_server_mode

Uruchamianie prostego serwera (Flask/FastAPI) i wyświetlanie wyników
w oknie przeglądarki. Przydatne gdy chcesz GUI web zamiast PyQt.
"""

from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def index():
    html = """
    <html>
      <head><title>WyszukiwaczPromocji Server Mode</title></head>
      <body>
        <h1>Witaj w trybie serwera!</h1>
        <p>Tutaj można pobierać wyniki, sterować scrapowaniem przez przeglądarkę.</p>
      </body>
    </html>
    """
    return render_template_string(html)

def run_server_mode():
    app.run(debug=True, port=8080)

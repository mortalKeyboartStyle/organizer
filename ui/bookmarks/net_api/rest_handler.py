"""
rest_handler.py
Keyword: net_api_rest

Możliwość wywoływania scrapowania / pobierania wyników przez interfejs HTTP.
Przykład z Flask, uproszczony.
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

# Prosty "global" storage – w rzeczywistości podłącz do bazy czy main_window
STORAGE = {
    "results": []
}

@app.route("/scrape", methods=["POST"])
def scrape_endpoint():
    data = request.json
    url = data.get("url")
    if not url:
        return jsonify({"error": "No URL provided"}), 400
    # Tu: wywołanie realnego scrapingu, np. main_window start_scraping
    STORAGE["results"].append({"url": url, "status": "mock_scraped"})
    return jsonify({"message": "Scraping started", "url": url}), 200

@app.route("/results", methods=["GET"])
def get_results():
    return jsonify(STORAGE["results"]), 200

def run_rest_api():
    """
    Uruchamia serwer Flask (np. python -m net_api.rest_handler).
    """
    app.run(debug=True, port=5000)

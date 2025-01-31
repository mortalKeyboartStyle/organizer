"""
headless_handler.py
Keyword: fuzzscrap_headless

Automatyczne klikanie przycisków, logowanie, zbieranie linków
z użyciem Selenium / Playwright w trybie headless.
Poniższy przykład - Selenium + Chrome.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def headless_browse(url):
    """
    Uruchamia Chrome w trybie headless, wchodzi na stronę,
    zwraca np. page_source.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get(url)
        page_source = driver.page_source
        return page_source
    finally:
        driver.quit()

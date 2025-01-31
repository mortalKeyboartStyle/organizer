from bs4 import BeautifulSoup

def parse_html(html, tag, attributes=None):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find_all(tag, attrs=attributes)

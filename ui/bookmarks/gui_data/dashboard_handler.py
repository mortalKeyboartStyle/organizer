"""
dashboard_handler.py
Keyword: gui_data_dashboard

Generowanie prostych wykresów (kołowy, słupkowy) np. przy użyciu PyQtGraph lub matplotlib.
Tu - atrapa, zwracająca fikcyjne dane do wykresów.
"""

def get_chart_data(links):
    """
    Zakładamy, że 'links' to lista linków. Zwracamy słownik:
    {
      "domain_counts": { "onet.pl": 10, "wp.pl": 5, ... },
      "some_other_metric": ...
    }
    """
    from collections import Counter
    domain_counter = Counter()
    for link in links:
        # Proste wyodrębnienie domeny
        domain = link.split("//")[-1].split("/")[0]
        domain_counter[domain] += 1

    return {
        "domain_counts": dict(domain_counter)
    }

def generate_pie_data(domain_counts):
    """
    Zwraca listę krotek (etykieta, wartość) do wykresu kołowego.
    """
    return list(domain_counts.items())

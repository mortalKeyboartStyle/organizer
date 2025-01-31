"""
timeline_handler.py
Keyword: gui_data_timeline

Wizualne przedstawienie, kiedy link został znaleziony (timeline).
Na razie atrapa, przechowuje listę (timestamp, link).
"""

import time

def add_link_to_timeline(timeline_data, link):
    """
    timeline_data: lista krotek (timestamp, link).
    """
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    timeline_data.append((now, link))

def get_timeline_display(timeline_data):
    """
    Zwraca sformatowany string z timeline.
    """
    lines = []
    for entry in timeline_data:
        ts, link = entry
        lines.append(f"{ts} -> {link}")
    return "\n".join(lines)

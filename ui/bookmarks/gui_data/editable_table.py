"""
editable_table.py
Keyword: gui_data_editable_table

Możliwość klikania w komórki i zmieniania wartości.
"""

from PyQt6.QtWidgets import QAbstractItemView

def make_table_editable(table):
    """
    Umożliwia edycję komórek w QTableWidget.
    """
    table.setEditTriggers(QAbstractItemView.EditTrigger.AllEditTriggers)

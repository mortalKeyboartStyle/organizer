"""
dragdrop_handler.py
Keyword: gui_data_dragdrop

Możliwość przeciągania linków do innego miejsca, sortowania w tabeli 'drag & drop'.
Implementacja zależy mocno od PyQt eventów. Tu prosta atrapa.
"""

def enable_drag_drop_for_table(table):
    """
    Ustawia właściwości QTableWidget, by obsługiwać drag & drop.
    """
    table.setDragDropMode(table.DragDropMode.InternalMove)
    table.setDragEnabled(True)
    table.setAcceptDrops(True)
    table.setDropIndicatorShown(True)
    # W razie potrzeby można podpiąć eventy 'dragEnterEvent', 'dropEvent'.

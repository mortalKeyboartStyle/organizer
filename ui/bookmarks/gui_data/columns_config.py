"""
columns_config.py
Keyword: gui_data_columns

Użytkownik może dodać kolumny do tabeli, np. "ocena", "kategoria".
"""

def add_custom_column(main_window, column_name):
    """
    Dodaje kolumnę do main_window.results_table (lub innej tabeli).
    """
    current_col_count = main_window.results_table.columnCount()
    main_window.results_table.insertColumn(current_col_count)
    main_window.results_table.setHorizontalHeaderItem(current_col_count, main_window.create_table_header(column_name))

def remove_custom_column(main_window, column_index):
    """
    Usuwa kolumnę z tabeli po indeksie.
    """
    main_window.results_table.removeColumn(column_index)

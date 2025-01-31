# ui/bookmarks/nettools/code_scanner.py
import ast

DANGEROUS_FUNCTIONS = ["eval", "exec", "compile", "__import__"]

def scan_code_for_danger(path_to_file):
    """
    Wczytuje plik .py, parsuje AST i sprawdza wystąpienie niebezp. funkcji.
    Zwraca listę ostrzeżeń albo pustą listę, jeśli OK.
    """
    warnings = []
    try:
        with open(path_to_file, "r", encoding="utf-8") as f:
            source = f.read()

        tree = ast.parse(source, filename=path_to_file)
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and hasattr(node.func, 'id'):
                func_name = node.func.id
                if func_name in DANGEROUS_FUNCTIONS:
                    warnings.append(f"Użycie {func_name} w linii {node.lineno}")
        return warnings
    except Exception as e:
        return [f"[CodeScanner] Błąd: {e}"]

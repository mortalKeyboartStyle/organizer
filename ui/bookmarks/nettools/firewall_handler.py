# ui/bookmarks/nettools/firewall_handler.py
import subprocess

def list_iptables_rules():
    """
    Przykładowa funkcja odczytująca aktualne reguły iptables.
    Zwraca string z listą lub błąd.
    """
    try:
        output = subprocess.check_output(["iptables", "-L"], text=True)
        return f"[Firewall] Bieżące reguły:\n{output}"
    except Exception as e:
        return f"[Firewall Error] {e}"

def add_block_rule(ip):
    """
    Dodaje regułę, by blokować ruch przychodzący z danego IP.
    Wymaga uprawnień roota. Używać ostrożnie w środowisku testowym.
    """
    try:
        subprocess.check_call(["iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"])
        return f"[Firewall] Zablokowano IP: {ip}"
    except Exception as e:
        return f"[Firewall] Błąd blokowania IP {ip}: {e}"

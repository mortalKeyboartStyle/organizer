# ui/bookmarks/nettools/ids_handler.py
try:
    from scapy.all import sniff
except ImportError:
    # jeżeli scapy nie jest zainstalowane
    pass

def run_simple_ids(interface="eth0", packet_count=10):
    """
    Przykład przechwytywania pakietów w stylu IDS.
    Zwraca listę prostych opisów pakietów.
    UWAGA: wymaga scapy i odpowiednich uprawnień.
    """
    results = []
    try:
        packets = sniff(iface=interface, count=packet_count, timeout=15)
        for pkt in packets:
            proto = pkt.summary()
            results.append(proto)
        return results
    except Exception as e:
        return [f"[IDS] Błąd przechwytywania: {e}"]

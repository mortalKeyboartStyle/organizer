# ui/bookmarks/nettools/hardening_manager.py
import subprocess

REQUIRED_SYSCTLS = {
    "net.ipv4.conf.all.rp_filter": "1",
    "net.ipv4.tcp_syncookies": "1",
}

def check_sysctl():
    """
    Sprawdza wartości kluczowych parametrów sysctl.
    Zwraca listę komunikatów.
    """
    messages = []
    for key, desired_val in REQUIRED_SYSCTLS.items():
        try:
            val = subprocess.check_output(["sysctl", "-n", key], text=True).strip()
            if val == desired_val:
                messages.append(f"[OK] {key} = {val}")
            else:
                messages.append(f"[WARN] {key} = {val}, oczekiwano {desired_val}")
        except Exception as e:
            messages.append(f"[ERROR] sysctl {key}: {e}")
    return messages

def apply_sysctl_fix(key, value):
    """
    Przykład narzędzia do zmiany parametru sysctl.
    """
    try:
        subprocess.check_call(["sysctl", f"{key}={value}"])
        return f"[Hardening] Ustawiono {key} = {value}"
    except Exception as e:
        return f"[Hardening] Błąd ustawiania {key}: {e}"

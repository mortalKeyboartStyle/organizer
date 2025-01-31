import logging
from PyQt6.QtWidgets import QMessageBox

# Importy z Twoich modułów nettools:
from ui.bookmarks.nettools.firewall_handler import list_iptables_rules, add_block_rule
from ui.bookmarks.nettools.ids_handler import run_simple_ids
from ui.bookmarks.nettools.code_scanner import scan_code_for_danger
from ui.bookmarks.nettools.gpu_cracker import run_gpu_cracking
from ui.bookmarks.nettools.container_env import run_ephemeral_container
from ui.bookmarks.nettools.keylogger_handler import start_keylogger_mock
from ui.bookmarks.nettools.hardening_manager import check_sysctl, apply_sysctl_fix

class NettoolsMethods:
    """
    Klasa z metodami logiki dla zakładki [nettools].
    Obejmuje:
     - firewall
     - IDS
     - code scanner
     - GPU cracking
     - container ephemeral environment
     - keylogger
     - hardening manager

    W pliku nettools_tab.py budujemy UI (przyciski),
    a tu mamy implementację metod wywoływanych po kliknięciu.
    """

    def run_firewall_demo(self):
        """
        Pokazowe wyświetlenie aktualnych reguł firewall (iptables).
        """
        try:
            output = list_iptables_rules()
            QMessageBox.information(self, "Firewall Demo", f"Obecne reguły:\n{output}")
        except Exception as e:
            logging.exception("Błąd w run_firewall_demo")
            QMessageBox.critical(self, "Firewall Error", str(e))

    def run_block_ip(self, ip: str):
        """
        Blokowanie ruchu z danego IP (iptables).
        """
        try:
            result = add_block_rule(ip)
            QMessageBox.information(self, "Firewall Demo", result)
        except Exception as e:
            logging.exception("Błąd w run_block_ip")
            QMessageBox.critical(self, "Firewall Error", str(e))

    def run_ids_demo(self):
        """
        Uruchomienie prostego IDS (np. sniffera) w stylu run_simple_ids.
        """
        try:
            packets_info = run_simple_ids(interface="eth0", packet_count=5)
            info_text = "\n".join(packets_info)
            QMessageBox.information(self, "Prosty IDS", f"Przechwycone pakiety:\n{info_text}")
        except Exception as e:
            logging.exception("Błąd w run_ids_demo")
            QMessageBox.critical(self, "IDS Error", str(e))

    def run_code_scanner_demo(self):
        """
        Prosty skaner bezpieczeństwa kodu Python (AST).
        """
        try:
            warnings = scan_code_for_danger("/path/to/some_script.py")
            if warnings:
                text = "Znaleziono niebezpieczne wywołania:\n" + "\n".join(warnings)
            else:
                text = "Nie znaleziono niebezpiecznych wywołań."
            QMessageBox.information(self, "Code Security Scanner", text)
        except Exception as e:
            logging.exception("Błąd w run_code_scanner_demo")
            QMessageBox.critical(self, "Code Scanner Error", str(e))

    def run_gpu_cracking_demo(self):
        """
        Uruchomienie pseudologic 'GPU cracking' (mock).
        """
        try:
            hash_str = "testhash"
            result = run_gpu_cracking(hash_str, wordlist_path="wordlist.txt")
            QMessageBox.information(self, "GPU Cracking", result)
        except Exception as e:
            logging.exception("Błąd w run_gpu_cracking_demo")
            QMessageBox.critical(self, "GPU Cracker Error", str(e))

    def run_container_env_demo(self):
        """
        Przykład ephemeral container environment (Docker).
        """
        try:
            msg = run_ephemeral_container(image_name="ubuntu:latest", lifetime=10)
            QMessageBox.information(self, "Container Env", msg)
        except Exception as e:
            logging.exception("Błąd w run_container_env_demo")
            QMessageBox.critical(self, "Container Env Error", str(e))

    def run_keylogger_demo(self):
        """
        Atrapa keyloggera - start Keylogger mock (pynput).
        """
        try:
            result = start_keylogger_mock()
            QMessageBox.information(self, "Keylogger Demo", result)
        except Exception as e:
            logging.exception("Błąd w run_keylogger_demo")
            QMessageBox.critical(self, "Keylogger Error", str(e))

    def run_hardening_demo(self):
        """
        Przykład twardych ustawień sysctl.
        """
        try:
            checks = check_sysctl()
            text = "\n".join(checks)
            QMessageBox.information(self, "Hardening Manager", f"Wynik sprawdzania:\n{text}")

            # ewentualnie apply_sysctl_fix(...) do wymuszenia
        except Exception as e:
            logging.exception("Błąd w run_hardening_demo")
            QMessageBox.critical(self, "Hardening Error", str(e))

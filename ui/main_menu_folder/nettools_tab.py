from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QToolBox, QPushButton
)

def build_nettools_tab(main_window):
    """
    Tworzy widget [nettools_page] i wstawia QToolBox z 7 sekcjami:
      1) Firewall
      2) Prosty IDS
      3) Code security scanner
      4) GPU cracking
      5) Container ephemeral
      6) Keylogger
      7) Hardening

    Na koniec dołącza ten widget do main_window.main_toolbox jako "[nettools]".

    Wszystkie metody logiki (run_firewall_demo, run_block_ip, itd.) 
    żyją w klasie NettoolsMethods (dziedziczonej przez MainWindow).
    """

    # Główny widget i layout
    nettools_page = QWidget()
    nettools_layout = QVBoxLayout(nettools_page)

    # Tworzymy QToolBox, w którym będą poszczególne sekcje
    nettools_toolbox = QToolBox()
    nettools_layout.addWidget(nettools_toolbox)

    # --- 1) Firewall ---
    firewall_widget = QWidget()
    fw_layout = QVBoxLayout(firewall_widget)

    # Przycisk - "Pokaż reguły Firewall"
    fw_placeholder_btn = QPushButton("Pokaż reguły Firewall")
    # Metoda jest w NettoolsMethods -> MainWindow
    fw_placeholder_btn.clicked.connect(main_window.run_firewall_demo)
    fw_layout.addWidget(fw_placeholder_btn)

    # Przycisk - "Blokuj IP 8.8.8.8"
    block_ip_btn = QPushButton("Blokuj IP 8.8.8.8")
    block_ip_btn.clicked.connect(lambda: main_window.run_block_ip("8.8.8.8"))
    fw_layout.addWidget(block_ip_btn)

    firewall_widget.setLayout(fw_layout)
    nettools_toolbox.addItem(firewall_widget, "Skrypt do firewall")

    # --- 2) Prosty IDS ---
    ids_widget = QWidget()
    ids_layout = QVBoxLayout(ids_widget)

    ids_placeholder_btn = QPushButton("Placeholder - Prosty IDS")
    ids_placeholder_btn.clicked.connect(main_window.run_ids_demo)
    ids_layout.addWidget(ids_placeholder_btn)

    ids_widget.setLayout(ids_layout)
    nettools_toolbox.addItem(ids_widget, "Prosty IDS")

    # --- 3) Code security scanner ---
    codesec_widget = QWidget()
    codesec_layout = QVBoxLayout(codesec_widget)

    codesec_placeholder_btn = QPushButton("Placeholder - Code security scanner")
    codesec_placeholder_btn.clicked.connect(main_window.run_code_scanner_demo)
    codesec_layout.addWidget(codesec_placeholder_btn)

    codesec_widget.setLayout(codesec_layout)
    nettools_toolbox.addItem(codesec_widget, "Code security scanner")

    # --- 4) GPU cracking panel ---
    gpucrack_widget = QWidget()
    gpu_layout = QVBoxLayout(gpucrack_widget)

    gpu_placeholder_btn = QPushButton("Placeholder - GPU cracking panel")
    gpu_placeholder_btn.clicked.connect(main_window.run_gpu_cracking_demo)
    gpu_layout.addWidget(gpu_placeholder_btn)

    gpucrack_widget.setLayout(gpu_layout)
    nettools_toolbox.addItem(gpucrack_widget, "GPU cracking panel")

    # --- 5) Container ephemeral environment ---
    container_widget = QWidget()
    container_layout = QVBoxLayout(container_widget)

    container_placeholder_btn = QPushButton("Placeholder - Container ephemeral environment")
    container_placeholder_btn.clicked.connect(main_window.run_container_env_demo)
    container_layout.addWidget(container_placeholder_btn)

    container_widget.setLayout(container_layout)
    nettools_toolbox.addItem(container_widget, "Container ephemeral env")

    # --- 6) Keylogger demo ---
    keylogger_widget = QWidget()
    keylog_layout = QVBoxLayout(keylogger_widget)

    keylog_placeholder_btn = QPushButton("Placeholder - Keylogger demo")
    keylog_placeholder_btn.clicked.connect(main_window.run_keylogger_demo)
    keylog_layout.addWidget(keylog_placeholder_btn)

    keylogger_widget.setLayout(keylog_layout)
    nettools_toolbox.addItem(keylogger_widget, "Keylogger demo")

    # --- 7) Hardening manager ---
    hardening_widget = QWidget()
    hardening_layout = QVBoxLayout(hardening_widget)

    hard_placeholder_btn = QPushButton("Placeholder - Hardening manager")
    hard_placeholder_btn.clicked.connect(main_window.run_hardening_demo)
    hardening_layout.addWidget(hard_placeholder_btn)

    hardening_widget.setLayout(hardening_layout)
    nettools_toolbox.addItem(hardening_widget, "Hardening manager")

    # Ustawiamy layout i dołączamy do main_window.main_toolbox
    nettools_page.setLayout(nettools_layout)
    main_window.main_toolbox.addItem(nettools_page, "[nettools]")

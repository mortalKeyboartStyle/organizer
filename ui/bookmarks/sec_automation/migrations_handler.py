"""
migrations_handler.py
Keyword: sec_automation_migrations

Automatyczne przełączanie schematów bazy (SQLite w tym przykładzie).
Prosty system 'versji' w tabeli migrations.
"""

import sqlite3
import os

DB_FILE = "promo_data.db"

def run_migration():
	"""
	Sprawdza tabelę 'migrations', w razie potrzeby aktualizuje schemat.
	"""
	if not os.path.exists(DB_FILE):
		return

	conn = sqlite3.connect(DB_FILE)
	c = conn.cursor()
	c.execute("CREATE TABLE IF NOT EXISTS migrations (version INTEGER UNIQUE)")
	conn.commit()

	# Ustalmy, że 'latest_version' = 2. 
	# Jeśli w migrations brakuje 1 i 2, to je uruchamiamy.
	for version_needed in [1, 2]:
		c.execute("SELECT version FROM migrations WHERE version = ?", (version_needed,))
		if not c.fetchone():
			apply_single_migration(c, version_needed)
			c.execute("INSERT INTO migrations (version) VALUES (?)", (version_needed,))
			conn.commit()
	conn.close()

def apply_single_migration(cursor, version):
	"""
	Uruchamia migrację zależnie od version.
	"""
	if version == 1:
		# przykładowo: ALTER TABLE, CREATE TABLE
		cursor.execute("CREATE TABLE IF NOT EXISTS plugin_data (id INTEGER PRIMARY KEY, name TEXT)")
	elif version == 2:
		# inna migracja
		cursor.execute("ALTER TABLE plugin_data ADD COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP")

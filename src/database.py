import sqlite3

dbPath = "../data.db"

conn = sqlite3.connect(dbPath)
cursor = conn.cursor()


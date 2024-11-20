import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.files
from anvil.files import data_files
import anvil.server
import sqlite3


@anvil.server.callable
def get_gefaengnisse(rows="*"):
  conn = sqlite3.connect(data_files['gefaengnis.db'])
  cursor = conn.cursor()
  res = list(cursor.execute(f"SELECT {rows} FROM Gefaengnis"))
  print(res)
  return res

@anvil.server.callable
def get_direktor():
  conn = sqlite3.connect(data_files['gefaengnis.db'])
  cursor = conn.cursor()
  res = list(cursor.execute(f"SELECT direktor FROM Verwaltung"))
  print(res)
  return res

@anvil.server.callable
def get_freie_zellen():
  conn = sqlite3.connect(data_files['gefaengnis.db'])
  cursor = conn.cursor()
  res = list(cursor.execute(f"SELECT anzahl_freie_zellen FROM Verwaltung"))
  print(res)
  return res
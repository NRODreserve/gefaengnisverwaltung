from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run before the form opens.
    gefaengnis_daten = anvil.server.call('get_gefaengnisse', "namen, gefaengnis_ID")
    self.gefaengnisse_drop_down.items = [(namen, gefaengnis_ID) for namen, gefaengnis_ID in gefaengnis_daten]
    self.label_direktor.text = anvil.server.call('get_direktor')
    self.label_freie_zellen.text = anvil.server.call('get_freie_zellen')
    self.repeating_zellen.items = [{'zellennummer': 'TODO', 'anzahl_häftlinge': 'TODO'}, 
                                   {'zellennummer': 'TODO', 'anzahl_häftlinge': 'TODO'}]

  def gefaengnisse_drop_down_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

 



  
 

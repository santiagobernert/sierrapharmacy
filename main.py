from data_extraction.extract import find_in_text
from interface.interface import App
from webautomation.automation import place_order

app = App(find_in_text, place_order)
app.run()
from data_extraction.extract import find_in_text
from interface.interface import run

app = run(find_in_text)
app.mainloop()
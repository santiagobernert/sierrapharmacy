'''import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import PyPDF2

def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_preview_label.config(text=f"Selected File: {file_path}")

def display_pdf_content(file_path):
    try:
        pdf_file = open(file_path, "rb")
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        
        num_pages = pdf_reader.numPages
        pdf_content = ""
        
        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            pdf_content += page.extractText() + "\n"
        
        pdf_file.close()
        
        pdf_content_text.config(state=tk.NORMAL)
        pdf_content_text.delete("1.0", tk.END)
        pdf_content_text.insert(tk.END, pdf_content)
        pdf_content_text.config(state=tk.DISABLED)
    except Exception as e:
        pdf_content_text.config(state=tk.NORMAL)
        pdf_content_text.delete("1.0", tk.END)
        pdf_content_text.insert(tk.END, f"Error reading PDF: {str(e)}")
        pdf_content_text.config(state=tk.DISABLED)


def place_order_and_print():
    stop_notes = stop_notes_entry.get()
    order_reference = order_reference_entry.get()
    delivery_option = delivery_option_combobox.get()
    
    print(f"Stop Notes: {stop_notes}")
    print(f"Order Reference: {order_reference}")
    print(f"Delivery Option: {delivery_option}")
    
root = tk.Tk()
root.title("Sierra Pharmacy - Order automation")
root.geometry("600x600")
root.configure(padx=10, pady=10)

style = ttk.Style()
style.configure('Rounded.TEntry', borderwidth=1, relief="solid", padding=5, bordercolor="#ccc", borderradius=10)
style.configure("Rounded.TMenubutton", padding=(10, 5))
arrow_image = tk.PhotoImage(file="interface/arrow.png")  # Provide the path to your arrow image
style.layout("Rounded.TMenubutton", [
    ("Rounded.Menubutton.button", {"children": [
        ("Rounded.Menubutton.indicator", {"side": "right", "sticky": ""}),
    ]}),
])

title_label = tk.ctk.CTkLabel(root, text="Automate Your Order", font=("Helvetica", 16))
title_label.grid(row=0, columnspan=2, pady=10)

stop_notes_label = tk.ctk.CTkLabel(root, text="Stop notes:")
stop_notes_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

stop_notes_entry = ttk.ctk.CTkEntry(root, style="Rounded.TEntry", width=50)
stop_notes_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=5)

order_reference_label = tk.ctk.CTkLabel(root, text="Order reference:")
order_reference_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

order_reference_entry = ttk.ctk.CTkEntry(root, style="Rounded.TEntry", width=50)
order_reference_entry.grid(row=2, column=1, padx=10, pady=5)


delivery_option_label1 = tk.ctk.CTkLabel(root, text="Delivery Option:")
delivery_option_label1.grid(row=3, column=0, padx=10, pady=5, sticky="e")

delivery_options = ["Next Day", "Next Day AM", "Next Day PM"]
delivery_option_combobox = tk.StringVar()
delivery_option_combobox.set(delivery_options[0])
delivery_option_dropdown = tk.ctk.CtkOptionMenu(root, delivery_option_combobox, *delivery_options)
delivery_option_dropdown["menu"].configure(bg="white")  # Set background color
delivery_option_dropdown.config(image=arrow_image)
delivery_option_dropdown.grid(row=3, column=1, padx=10, pady=5, sticky='w')

browse_button = tk.ctk.CTkButton(root, text="Browse File", command=browse_file)
browse_button.grid(row=4, columnspan=2, padx=10, pady=10)

file_preview_label = tk.ctk.CTkLabel(root, text="Selected File: None")
file_preview_label.grid(row=5, columnspan=2, padx=10, pady=10)

pdf_content_text = tk.Text(root, wrap=tk.WORD, height=10, width=40)
pdf_content_text.grid(row=6, columnspan=2, padx=10, pady=5)
pdf_content_text.config(state=tk.DISABLED)

place_order_button = tk.ctk.CTkButton(root, text="Place order and print", command=place_order_and_print)
place_order_button.grid(row=7, columnspan=2, padx=10, pady=10)

root.mainloop()'''

import customtkinter as ctk
from tkinter import filedialog
import PyPDF2

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        file_preview_label.text = f"Selected File: {file_path}"
        display_pdf_content(file_path)

def display_pdf_content(file_path):
    try:
        pdf_file = open(file_path, "rb")
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)

        num_pages = pdf_reader.numPages
        pdf_content = ""

        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            pdf_content += page.extractText() + "\n"

        pdf_file.close()

        pdf_content_text.text = pdf_content
    except Exception as e:
        pdf_content_text.text = f"Error reading PDF: {str(e)}"

def place_order_and_print():
    stop_notes = stop_notes_entry.text
    order_reference = order_reference_entry.text
    delivery_option = delivery_option_var.get()

    # Here, you can implement the logic for placing the order and printing it
    # Replace this print statement with your actual implementation
    print(f"Stop Notes: {stop_notes}")
    print(f"Order Reference: {order_reference}")
    print(f"Delivery Option: {delivery_option}")

app = ctk.CTk()
app.title("Automate Your Order")
app.geometry("600x600")
app.resizable(height=False, width=False)

# Create a title label centered in the window
title_label = ctk.CTkLabel(app, text="Automate Your Order", font=("Helvetica", 26))
title_label.grid(row=0, columnspan=2, pady=10)

stop_notes_label = ctk.CTkLabel(app, text="Stop notes:")
stop_notes_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

stop_notes_entry = ctk.CTkEntry(app, width=400, corner_radius=5)  # Make the entry widget wider
stop_notes_entry.grid(row=1, column=1, padx=10, pady=5)

order_reference_label = ctk.CTkLabel(app, text="Order reference:")
order_reference_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

order_reference_entry = ctk.CTkEntry(app, width=400, corner_radius=5)  # Make the entry widget wider
order_reference_entry.grid(row=2, column=1, padx=10, pady=5)

delivery_option_label = ctk.CTkLabel(app, text="Delivery Option:")
delivery_option_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")

delivery_options = ["Next Day", "Next Day AM", "Next Day PM"]

# Custom style for OptionMenu with an arrow image
delivery_option_menu = ctk.CTkOptionMenu(app, values=delivery_options, corner_radius=5)
delivery_option_menu.grid(row=3, column=1, padx=10, pady=5, sticky='w')

browse_button = ctk.CTkButton(app, text="Browse File", command=browse_file, corner_radius=5)
browse_button.grid(row=4, column=1, padx=10, pady=5)

file_preview_label = ctk.CTkLabel(app, text="Selected File: None")
file_preview_label.grid(row=5, column=1, padx=10, pady=5)

pdf_name = ""
pdf_content_text = ctk.CTkLabel(app, text=pdf_name, height=10, width=40)
pdf_content_text.grid(row=6, columnspan=2, padx=10, pady=5)

place_order_button = ctk.CTkButton(app, text="Place order and print", command=place_order_and_print, corner_radius=5)
place_order_button.grid(row=7, columnspan=2, padx=10, pady=10)

app.mainloop()
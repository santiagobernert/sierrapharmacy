import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog
import PyPDF2

def browse_file(file_preview_label, pdf_content_text, find_in_text):
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")], title="Open PDF file")
    if file_path:
        file_preview_label.configure(text=f"Selected File: {file_path}")
        print(file_path)
        display_pdf_content(file_path, pdf_content_text, find_in_text)

def display_pdf_content(file_path, pdf_content_text, find_in_text):
    try:
        pdf_reader = PyPDF2.PdfReader(file_path)

        num_pages = len(pdf_reader.pages)
        pdf_content = ""

        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            pdf_content += page.extract_text() + "\n"

        text = '\n'.join(pdf_content.splitlines()[2:-2])
        pdf_content_text.insert("0.0", text)
        data = find_in_text(text)
        pdf_content_text.insert("end", '\n\n' + str(data).strip("}{").replace("',", "\n").replace("'", ""))
        pdf_content_text.configure(state='disabled')


    except Exception as e:
        print(e)
        pdf_content_text.insert( '0.0', f"Error reading PDF: {str(e)}")

def place_order_and_print(stop_notes_entry, order_reference_entry, delivery_option_var):
    stop_notes = stop_notes_entry.text
    order_reference = order_reference_entry.text
    delivery_option = delivery_option_var.get()

    # Here, you can implement the logic for placing the order and printing it
    # Replace this print statement with your actual implementation
    print(f"Stop Notes: {stop_notes}")
    print(f"Order Reference: {order_reference}")
    print(f"Delivery Option: {delivery_option}")

def run(find_in_text):
    app = ctk.CTk()
    app.title("Sierra Pharmacy Order Automation")
    app.geometry("600x600")
    app.maxsize(width=600, height=600)
    app.minsize(width=600, height=600)
    app.grid_columnconfigure((0,1), weight=1)
    app.resizable(height=False, width=False)
    app._set_appearance_mode("dark")

    title_label = ctk.CTkLabel(app, text="Automate Your Order", font=("Helvetica", 26))
    title_label.grid(row=0, columnspan=2, pady=10)

    stop_notes_label = ctk.CTkLabel(app, text="Stop notes:")
    stop_notes_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

    stop_notes_entry = ctk.CTkEntry(app, width=400, corner_radius=5)  # Make the entry widget wider
    stop_notes_entry.grid(row=1, column=1, padx=10, pady=5, sticky='w')

    order_reference_label = ctk.CTkLabel(app, text="Order reference:")
    order_reference_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

    order_reference_entry = ctk.CTkEntry(app, width=400, corner_radius=5)  # Make the entry widget wider
    order_reference_entry.grid(row=2, column=1, padx=10, pady=5, sticky='w')

    delivery_option_label = ctk.CTkLabel(app, text="Delivery Option:")
    delivery_option_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")

    delivery_options = ["Next Day", "Next Day AM", "Next Day PM"]

    delivery_option_menu = ctk.CTkOptionMenu(app, values=delivery_options, corner_radius=5)
    delivery_option_menu.grid(row=3, column=1, padx=10, pady=5, sticky='w')

    browse_button = ctk.CTkButton(app, text="Browse File", command=lambda:browse_file(file_preview_label, pdf_content_text, find_in_text), corner_radius=5)
    browse_button.grid(row=4, columnspan=2, padx=10, pady=5)

    file_preview_label = ctk.CTkLabel(app, text="Selected File: None")
    file_preview_label.grid(row=5, columnspan=2, padx=10, pady=5)

    pdf_content_text = ctk.CTkTextbox(app, height=300, width=500, corner_radius=5)
    pdf_content_text.grid(row=6, columnspan=2, padx=10, pady=5)

    place_order_button = ctk.CTkButton(app, text="Place order and print", command=place_order_and_print, corner_radius=5)
    place_order_button.grid(row=7, columnspan=2, padx=10, pady=10)

    return app
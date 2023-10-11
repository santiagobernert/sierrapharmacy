import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog
import PyPDF2

class App():
    def __init__(self, find_in_text, place_order):
        self.find_in_text = find_in_text
        self.place_order = place_order


        self.app = ctk.CTk()
        self.app.title("Sierra Pharmacy Order Automation")
        self.app.geometry("600x600")
        self.app.maxsize(width=600, height=600)
        self.app.minsize(width=600, height=600)
        self.app.grid_columnconfigure((0,1,2,3), weight=1)
        self.app.resizable(height=False, width=False)
        self.app._set_appearance_mode("dark")

        self.title_label = ctk.CTkLabel(self.app, text="Automate Your Order", font=("Helvetica", 26))
        self.title_label.grid(row=0, columnspan=4, pady=10)

        self.stop_notes_label = ctk.CTkLabel(self.app, text="Stop notes:")
        self.stop_notes_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

        self.stop_notes_entry = ctk.CTkEntry(self.app, width=350, corner_radius=5)  # Make the entry widget wider
        self.stop_notes_entry.grid(row=1, column=1, columnspan=3, padx=10, pady=5, sticky='w')

        self.order_reference_label = ctk.CTkLabel(self.app, text="Order reference:")
        self.order_reference_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

        self.order_reference_entry = ctk.CTkEntry(self.app, width=350, corner_radius=5)  # Make the entry widget wider
        self.order_reference_entry.grid(row=2, column=1, columnspan=3, padx=10, pady=5, sticky='w')

        self.delivery_option_label = ctk.CTkLabel(self.app, text="Delivery Option:")
        self.delivery_option_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")

        self.delivery_options = ["NextDay", "NextDayAM", "NextDayPM"]

        self.delivery_option_menu = ctk.CTkOptionMenu(self.app, values=self.delivery_options, corner_radius=5)
        self.delivery_option_menu.grid(row=3, column=1, padx=10, pady=5, sticky='w')

        self.time_ready_label = ctk.CTkLabel(self.app, text="Ready by time:")
        self.time_ready_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")

        self.hour_options = ["12", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11"]
        self.minutes_options = ["00", "15", "30", "45"]
        self.daytime_options = ["AM", "PM"]

        self.hour_option_menu = ctk.CTkOptionMenu(self.app, values=self.hour_options, corner_radius=5, width=90)
        self.hour_option_menu.grid(row=4, column=1, padx=10, pady=5, sticky='w')
        self.minutes_option_menu = ctk.CTkOptionMenu(self.app, values=self.minutes_options, corner_radius=5, width=90)
        self.minutes_option_menu.grid(row=4, column=2, padx=10, pady=5, sticky='w')
        self.daytime_option_menu = ctk.CTkOptionMenu(self.app, values=self.daytime_options, corner_radius=5, width=90)
        self.daytime_option_menu.grid(row=4, column=3, padx=10, pady=5, sticky='w')


        self.browse_button = ctk.CTkButton(self.app, text="Browse File", command=lambda:self.browse_file(), corner_radius=5)
        self.browse_button.grid(row=5, columnspan=4, padx=10, pady=5)

        self.patient_name = ctk.CTkLabel(self.app, text="Patient name: None", text_color='white', bg_color='red', width=100, height=30, font=('Helvetica', 16), corner_radius=10)
        self.patient_name.grid(row=6, columnspan=4)

        self.file_preview_label = ctk.CTkLabel(self.app, text="Selected File: None")
        self.file_preview_label.grid(row=7, columnspan=4, padx=10, pady=5)

        self.pdf_content_text = ctk.CTkTextbox(self.app, height=150, width=500, corner_radius=5)
        self.pdf_content_text.grid(row=8, columnspan=4, padx=10, pady=5)

        self.result_label = ctk.CTkLabel(self.app, text="")
        self.result_label.grid(row=9, columnspan=4)

        self.place_order_button = ctk.CTkButton(self.app, text="Place order and print", command=lambda:self.place_order_and_print(self.display_pdf_content(self.file_preview_label.cget("text")[15:])), corner_radius=5)
        self.place_order_button.grid(row=10, columnspan=4, padx=10, pady=10)


    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")], title="Open PDF file")
        if file_path:
            self.file_preview_label.configure(text=f"Selected File: {file_path}")
            self.display_pdf_content(file_path)

    def display_pdf_content(self, file_path):
        try:
            pdf_reader = PyPDF2.PdfReader(file_path)

            num_pages = len(pdf_reader.pages)
            pdf_content = ""

            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                pdf_content += page.extract_text() + "\n"

            text = '\n'.join(pdf_content.splitlines()[2:-9])
            self.pdf_content_text.configure(state='normal')
            self.pdf_content_text.delete("0.0", "999.999")
            self.pdf_content_text.insert("0.0", text)
            data = self.find_in_text(text)
            self.patient_name.configure(text=f"Patient Name: {data['name']}", width=200)
            # pdf_content_text.insert("end", '\n\n' + str(data).strip("}{").replace("',", "\n").replace("'", ""))
            self.pdf_content_text.configure(state='disabled')
            
            return data


        except Exception as e:
            print(e)
            self.pdf_content_text.insert( '0.0', f"Error reading PDF: {str(e)}")
            return Exception()

    def place_order_and_print(self, data):
        data["stop_notes"] = self.stop_notes_entry.get()
        data["order_reference"] = self.order_reference_entry.get()
        data["delivery_option"] = self.delivery_option_menu.get()
        data["time_ready"] = f'{self.hour_option_menu.get()}:{self.minutes_option_menu.get()}:{self.daytime_option_menu.get()}'
        
        order = self.place_order(**data)
        if order:
            self.result_label.configure(text="Success", bg_color="green", text_color='white', width=80)
        else:
            self.result_label.configure(text="Error! Check address", bg_color="red", text_color='white', width=80)

    def run(self):
        self.app.mainloop()
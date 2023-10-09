import re
import PyPDF2

def get_data(file_path):
    data = {
        "Name": "PEREZ, FLORA", 
        "Sex": "F", 
        "Phone": "(909) 701-8832",
        "Street Address":" 9338 LOMITA DR", 
        "Apartment": "APT B", "Cell": "000-0000",
        "Addr2": "",
        "City": "Rancho Cucamonga",
        "State": "CA", 
        "Zip": "91701",
        "E-Mail": ""
        }
    try:
        pdf_reader = PyPDF2.PdfReader(file_path)

        num_pages = len(pdf_reader.pages)
        pdf_content = ""

        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            pdf_content += page.extract_text() + "\n"

        text = '\n'.join(pdf_content.splitlines()[2:-2])

        name = text.find("Patient")
        sex = text.find()
        phone = text.find()
        street_address = text.find()
        apartment = text.find()
        addr2 = text.find()
        city = text.find()
        state = text.find()
        zip = text.find()
        e_mail = text.find()

        return text

    except Exception as e:
        print(e)

def find_in_text(text):
    patron_name = r"Patient ([A-Z\s,]+)"
    patron_sex = r"Sex ([A-Z])"
    patron_phone = r"Phone \((\d{3})\) (\d{3}-\d{4})"
    patron_cell = r"Cell (\d{3}-\d{4})"
    patron_address = r"Address (\d+ [A-Z\s]+)"
    patron_apartment = r"APT ([a-zA-Z])"
    patron_addr2 = r"Addr2 (\d+ [A-Z\s]+)"
    patron_city = r"City ([a-zA-Z\s,]+)"
    patron_state = r"State ([A-Z]+)"
    patron_zip_code = r"Zip (\d+)"
    patron_email = r"E-Mail (\S+)"

    # Buscar coincidencias en el texto usando expresiones regulares
    resultado_name = re.search(patron_name, text)
    resultado_sex = re.search(patron_sex, text)
    resultado_phone = re.search(patron_phone, text)
    resultado_cell = re.search(patron_cell, text)
    resultado_address = re.search(patron_address, text)
    resultado_apartment = re.search(patron_apartment, text)
    resultado_addr2 = re.search(patron_addr2, text)
    resultado_city = re.search(patron_city, text)
    resultado_state = re.search(patron_state, text)
    resultado_zip_code = re.search(patron_zip_code, text)
    resultado_email = re.search(patron_email, text)

    # Crear un diccionario con los datos extraídos
    dat = {
        "name": resultado_name.group(1).strip()[:-1],
        "sex": resultado_sex.group(1),
        "phone": f"({resultado_phone.group(1)}) {resultado_phone.group(2)}",
        "cell": resultado_cell.group(1),
        "address": resultado_address.group(1).strip(),
        "apartment": resultado_apartment.group(1).strip() if resultado_apartment else "",
        "addr2": resultado_addr2.group(1).strip() if resultado_addr2 else "",
        "city": resultado_city.group(1).strip()[:-13],
        "state": resultado_state.group(1),
        "zip code": resultado_zip_code.group(1),
        "e_mail": resultado_email.group(1)
    }

    # Imprimir el diccionario resultante
    print(dat)



text = '''
Patient PEREZ, FLORA Sex F Phone (909) 701-8832
Address 9338 LOMITA DR APT B Cell 000-0000
Addr2 
City Rancho Cucamonga
State CA Zip 91701 
E-Mail gring@gmail.com
'''
find_in_text(text)


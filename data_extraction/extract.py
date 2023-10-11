import re

def find_in_text(text):
    name_pattern = r"Patient ([A-Z\s,]+)"
    sex_pattern = r"Sex ([A-Z])"
    phone_pattern = r"Phone \((\d{3})\) (\d{3}-\d{4})"
    cell_pattern = r"Cell \((\d{3})\) (\d{3}-\d{4})"
    address_pattern = r"Address (\d+ [A-Z\s]+)"
    apartment_pattern = r"(?:APT |#)([A-Z0-9]+)"
    addr2_pattern = r"Addr2 (\d+ [A-Z\s]+)"
    city_pattern = r"City ([A-Za-z]+ [A-Za-z]+)"
    state_pattern = r"State ([A-Z]+)"
    zip_code_pattern = r"Zip (\d+)"
    email_pattern = r"E-Mail ([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4})"

    search_name = re.search(name_pattern, text)
    search_sex = re.search(sex_pattern, text)
    search_phone = re.search(phone_pattern, text)
    search_cell = re.search(cell_pattern, text)
    search_address = re.search(address_pattern, text)
    search_apartment = re.search(apartment_pattern, text)
    search_addr2 = re.search(addr2_pattern, text)
    search_city = re.search(city_pattern, text)
    search_state = re.search(state_pattern, text)
    search_zip_code = re.search(zip_code_pattern, text)
    search_email = re.search(email_pattern, text)

    data = {
        "name": search_name.group(1).strip()[:-2] if search_name.group(1).strip().endswith(" S") else search_name.group(1).strip(),
        "sex": search_sex.group(1),
        "phone": f"({search_phone.group(1)}) {search_phone.group(2)}",
        "cell": f"({search_cell.group(1)}) {search_cell.group(2)}" if search_cell else "",
        "address": search_address.group(1).strip().split(' APT')[0] if 'APT' in search_address.group(1).strip() else search_address.group(1).strip()[:-2] if search_address.group(1).strip().endswith(' C') else search_address.group(1).strip(),
        "apartment": f"#{search_apartment.group(1).strip()}" if search_apartment else '',
        "addr2": search_addr2.group(1).strip() if search_addr2 else "",
        "city": search_city.group(1).strip().split(" DOB")[0],
        "state": search_state.group(1),
        "zip_code": search_zip_code.group(1),
        "e_mail": search_email.group(1) if search_email else ""
    }
    return data



text = '''
Patient HADDAD, RANIA Sex F Phone (626) 628-7594
Address 7980 MAYTEN AVE #1036 Cell (626) 628-7594
Addr2 FC Fax 000-0000
City Rancho Cucamonga DOB 04/12/1990 33 Wgt Hgt
State CA Zip 91730 Marital Status Residence Code 1
Ship To Pregnant? N Lactating?
E-Mail Cash ICD-10
HOH Disc
Employer Use Safety Caps Y Language English
SSN 215764173 CA Lic As of 07/10/18 HIPAA Sig on file
MBI Other Coverage 0 TPPDefault Plans PPW
'''
#find_in_text(text)


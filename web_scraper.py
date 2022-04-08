from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

# URL managment
url = "https://www.solotodo.cl/notebooks?offer_price_usd_end=532.6125&ordering=-score_general&"
url_client = urlopen(url)  # Agarra la pagina del url
read_html = url_client.read()  # Almaceno el html de la pag en una variable
url_client.close()  # cierra la conexión con la que se descarga la pag
# Beautiful Soup
soup = BeautifulSoup(read_html, "html.parser")  # Hace un beautifulsoup object de un html parsed

# CSV creation
a, b, c = "nombre", "specs", "precio"
pcs_scraper = open("pcs_scraper.csv", "w")
csv_writer = csv.writer(pcs_scraper)
csv_writer.writerow([a,b,c])

# Loop through information
pcs = soup.find_all("div", class_="d-flex flex-column category-browse-result")

for pc in pcs:
    name_pc = pc.h3.a.text
    print(name_pc)
    specs_pc = pc.find("div", class_="description-container").dlS.text
    print(specs_pc)
    price_pc = pc.find("div", class_="d-flex flex-row justify-content-between align-items-center mt-auto pt-2").div.a.text
    print(price_pc)
    # Write to CSV
    csv_writer.writerow([name_pc, specs_pc, price_pc])

pcs_scraper.close()
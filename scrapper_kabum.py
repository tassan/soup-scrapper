import unidecode
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.kabum.com.br/hardware/placa-de-video-vga?ordem=5&limite=100&pagina=1&string='

# opening connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()

# html parsing
page_soup = soup(page_html, "html.parser")

# grabs each product
containers = page_soup.find_all("div", {"class":"listagem-box"})

filename = 'csv_files/graphic_cards_kabum.csv'
csv = open(filename, "w")

headers = "brand, product_name, price\n"

csv.write(headers)

# loop through products and grab the gpu name
for container in containers:
    brand_container = container.find("div", {"class":"listagem-marca_avaliacao"})
    brand = brand_container.img["title"].replace("Logo ", "")
    product_name = unidecode.unidecode(container.a.img["title"])
    price_container = container.find("div", {"class":"listagem-precoavista"})
    price = f"{price_container.b.string}"
    
    # print("brand: " + brand)
    # print("product_name: " + product_name)
    # print("price: " + price)

    csv.write(brand.replace(",","") + "," + product_name.replace(",", "|") + "," + price.replace(".","").replace(",",".") + "\n")

csv.close
uClient.close()

print("Scrapping Completed!")

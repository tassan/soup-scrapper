from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=7709'

# opening connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()

# html parsing
page_soup = soup(page_html, "html.parser")

# grabs each product
containers = page_soup.find_all("div", {"class":"item-container"})

filename = "graphic_cards.csv"
csv = open(filename, "w")

headers = "brand, product_name, price \n"

csv.write(headers)

# loop through products and grab the gpu name
for container in containers:
    brand_container = container.find("a", {"class":"item-brand"})
    brand = brand_container.img["title"]
    product_name = container.a.img["title"]
    price_container = container.find("li", {"class":"price-current"})
    price = f"${price_container.strong.string}{price_container.sup.string}"
    
    # print("brand: " + brand)
    # print("product_name: " + product_name)
    # print("price: " + price)

    csv.write(brand + ";" + product_name.replace(",", "|") + ";" + price + "\n")

csv.close
uClient.close()
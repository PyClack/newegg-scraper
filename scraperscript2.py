'''
This is my first basic web scraper, designed as a teaching tool, and as an experiment.
It scrapes newegg's graphics cards homepage and returns the currently showcased graphics cards,
their prices, brands and shipping information before exporting that data to a csv file.

Newegg Scraper
Neil Clack
10-19-2017

'''
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards"

#Grabbing the page
uClient = uReq(my_url)

#Reading uCLient and saving contents as a variable called page_html (it is raw html code)
page_html = uClient.read()

#Close the web connection to uCLient
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

#Grabs graphics card containers / each product
containers = page_soup.find_all("div",{"class":"item-container"})

filename = "products.csv"

f = open(filename, "w")

headers = "Brand, Product Name, Price, Shipping\n"

f.write(headers)


for container in containers:

    brand = container.div.div.a.img["title"]

    title_container = container.find_all("a",{"class":"item-title"})
    product_name = title_container[0].text

    shipping_container = container.find_all("li",{"class":"price-ship"})
    shipping = shipping_container[0].text.strip()

    for item in page_soup.find_all('li',{'class':'price-current'}):
        price = item.strong.text+item.sup.text


    print("Brand: " + brand)
    print("Product name: " + product_name)
    print("Price: " + price)
    print("Shipping: " + shipping)

    f.write(brand + "," + product_name.replace(",","|") + "," + price + "," + shipping + "\n" )


f.close()


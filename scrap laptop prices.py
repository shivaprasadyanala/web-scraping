from bs4 import BeautifulSoup as soup  
from urllib.request import urlopen as uReq  
  
# Request from the webpage  
myurl = "https://www.flipkart.com/search?q=iphones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"  


uClient  = uReq(myurl)  
page_html = uClient.read()  
uClient.close()

page_soup = soup(page_html, features="html.parser") 

containers = page_soup.find_all("div",{"class": "_3pLy-c"}) 
print(containers)
for item in containers:
	print(item.find("div",{"class":"_4rR01T"}).text)
	print(item.find("div",{"class":"_30jeq3"}).text)


from bs4 import BeautifulSoup
from selenium import webdriver
import statistics
 
 

PATH = r'/usercode/chromedriver'
driver = webdriver.Chrome(PATH)
driver.get("https://www.net-a-porter.com/en-us/shop/clothing/jeans")

soup = BeautifulSoup(driver.page_source, 'html.parser')
# print(soup)
response = soup.find_all("span", {"itemprop" : "price"})
data = []

for item in response:
    data.append((item.text.strip('$')))

print(data)
 

 
p
import time
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.remote.remote_connection import LOGGER, logging
LOGGER.setLevel(logging.WARNING)

# Chrome Driver config
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument("--test-type")
options.add_argument('--headless')
options.add_argument('--silent')
# options.
driver = webdriver.Chrome(".\chromedriver.exe", chrome_options=options)


# utility Functions
def formatPrice(price):
    price = price[1:]
    price = price.split(',')
    price = ''.join(price)
    return price


def formatDiscount(discount):
    discount = discount.split('%')[0]
    return discount


titles = []
prices = []
ratings = []
discounts = []
links = []


url = "https://www.flipkart.com/"
driver.get(url)
# time.sleep(2)

# To close login model
# driver.find_element_by_css_selector("._2AkmmA._29YdH8").click()

text = input("Enter product name: ")
searchText = driver.find_element_by_class_name(
    "LM6RPg")        # to locate search box
searchText.send_keys(text)
searchText.send_keys(Keys.ENTER)

time.sleep(3)

for a in driver.find_elements_by_css_selector("._3liAhj"):
    print("*", end=" ")
    title = a.find_element_by_css_selector("._2cLu-l").get_attribute("title")
    link = a.find_element_by_css_selector("._2cLu-l").get_attribute("href")
    price = formatPrice(a.find_element_by_class_name("_1vC4OE").text)

    try:
        discount = formatDiscount(a.find_element_by_class_name(
            "VGWI6T").find_element_by_tag_name("span").text)
    except Exception:
        discount = 0

    try:
        rating = a.find_element_by_class_name("hGSR34").text
    except Exception:
        rating = 'NA'

    titles.append(title)
    prices.append(price)
    ratings.append(rating)
    discounts.append(discount)
    links.append(link)
print()


# To convert data into csv
df = pd.DataFrame({'Product Name': titles, 'Prices': prices,
                   'Rating': ratings, 'Discount %': discounts, 'Link': links})
text = text + '.csv'
df.to_csv(text, index=False, encoding='utf-8')
print("Check ", text)

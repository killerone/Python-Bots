import time
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

text = input("Enter product name: ")
# number = int(input("Enter number of pages to scan: "))
# Chrome Driver config
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument("--test-type")
options.add_argument('--headless')
options.add_argument('--silent')
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()


titles = []
prices = []
ratings = []
discounts = []
links = []
imageLinks = []


# utility Functions
def formatPrice(price):
    price = price[1:]
    price = price.split(',')
    price = ''.join(price)
    return price


def formatDiscount(discount):
    discount = discount.split('%')[0]
    return discount


url = "https://www.flipkart.com/search?q=" + text
driver.get(url)
# time.sleep(2)

# # To close login model
# driver.find_element_by_css_selector("._2AkmmA._29YdH8").click()


# searchText = driver.find_element_by_class_name(
#     "LM6RPg")        # to locate search box
# searchText.send_keys(text)
# searchText.send_keys(Keys.ENTER)

# time.sleep(3)

page = driver.find_elements_by_css_selector("._3liAhj")

if page:
    for item in page:
        print("*", end=" ")
        title = item.find_element_by_css_selector(
            "._2cLu-l").get_attribute("title")
        link = item.find_element_by_css_selector(
            "._2cLu-l").get_attribute("href")
        imageLink = item.find_element_by_css_selector(
            "._1Nyybr._30XEf0").get_attribute("src")
        price = formatPrice(
            item.find_element_by_class_name("_1vC4OE").text)

        try:
            discount = formatDiscount(item.find_element_by_class_name(
                "VGWI6T").find_element_by_tag_name("span").text)
        except Exception:
            discount = 0

        try:
            rating = item.find_element_by_class_name("hGSR34").text
        except Exception:
            rating = 'NA'

        titles.append(title)
        prices.append(price)
        ratings.append(rating)
        discounts.append(discount)
        links.append(link)
        imageLinks.append(imageLink)
    link = (driver.current_url).split("&page=")[0]
    page = driver.find_elements_by_css_selector("._3liAhj")
else:
    page = driver.find_elements_by_css_selector("._1UoZlX")
    for item in page:
        print("*", end=" ")
        link = item.find_element_by_css_selector(
            "._31qSD5").get_attribute("href")
        title = item.find_element_by_class_name("_3wU53n").text
        price = formatPrice(
            item.find_element_by_class_name("_1vC4OE").text)

        try:
            imageLink = item.find_element_by_css_selector(
                "._1Nyybr._30XEf0").get_attribute("src")

        except Exception:
            imageLink = " "

        try:
            discount = formatDiscount(item.find_element_by_class_name(
                "VGWI6T").find_element_by_tag_name("span").text)
        except Exception:
            discount = 0

        try:
            rating = item.find_element_by_class_name("hGSR34").text
        except Exception:
            rating = 'NA'

        titles.append(title)
        prices.append(price)
        ratings.append(rating)
        discounts.append(discount)
        links.append(link)
        imageLinks.append(imageLink)

    link = (driver.current_url).split("&page=")[0]
    page = driver.find_elements_by_css_selector("._1UoZlX")
print()


# To convert data into csv
df = pd.DataFrame({'Product Name': titles, 'Prices': prices,
                   'Rating': ratings, 'Discount %': discounts, 'Link': links, "Image Links": imageLinks})
text = text + '.csv'
df.to_csv(text, index=False, encoding='utf-8')
print("Check ", text)

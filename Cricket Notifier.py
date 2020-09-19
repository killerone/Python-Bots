from win10toast import ToastNotifier
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument("--test-type")
options.add_argument('--headless')
options.add_argument('--silent')
driver = webdriver.Chrome("chromedriver.exe", options=options)

toast = ToastNotifier()

url = "https://www.cricbuzz.com/"
driver.get(url)

driver.find_element_by_xpath(
    "/html/body/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/ul/li[1]/a/div[2]").click()

title = driver.find_element_by_xpath(
    "/html/body/div[1]/div[2]/div[4]/div[2]/h1").text
title = title.split(",")[0]

while 1:
    score = driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/h2").text

    crr = driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]/span[2]").text

    # Batsman 1 info
    batsman1name = driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[3]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/a").text
    batsman1score = driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[3]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]").text
    batsman1balls = driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[3]/div[2]/div[1]/div[2]/div[1]/div[2]/div[3]").text
    batsman1four = driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[3]/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]").text
    batsman1six = driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[3]/div[2]/div[1]/div[2]/div[1]/div[2]/div[5]").text
    batsman1sr = driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[3]/div[2]/div[1]/div[2]/div[1]/div[2]/div[6]").text

    # Batsman 2 info
    try:
        batsman2name = driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div[4]/div[3]/div[2]/div[1]/div[2]/div[1]/div[3]/div[1]/a").text
        batsman2score = driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div[4]/div[3]/div[2]/div[1]/div[2]/div[1]/div[3]/div[2]").text
        batsman2balls = driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div[4]/div[3]/div[2]/div[1]/div[2]/div[1]/div[3]/div[3]").text
        batsman2four = driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div[4]/div[3]/div[2]/div[1]/div[2]/div[1]/div[3]/div[4]").text
        batsman2six = driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div[4]/div[3]/div[2]/div[1]/div[2]/div[1]/div[3]/div[5]").text
        batsman2sr = driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div[4]/div[3]/div[2]/div[1]/div[2]/div[1]/div[3]/div[6]").text
    except Exception:
        batsman2name = "OUT"
        batsman2score = batsman2balls = batsman2four = batsman2six = batsman2sr = 0

    # Bowler info
    bowlername = driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[3]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/a").text
    bowlerover = driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[3]/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]").text
    bowlerrun = driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[3]/div[2]/div[1]/div[2]/div[2]/div[2]/div[4]").text
    bowlerwicket = driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[3]/div[2]/div[1]/div[2]/div[2]/div[2]/div[5]").text

    body = f"{score}    Crr: {crr}\n{batsman1name}\t{batsman1score} ({batsman1balls} | {batsman1four} | {batsman1six} | {batsman1sr})"
    body += f"\n{batsman2name}\t{batsman2score} ({batsman2balls} | {batsman2four} | {batsman2six} | {batsman2sr})"
    body += f"\n{bowlername}\t{bowlerover} ({bowlerrun}/{bowlerwicket})"
    # body = score + "  CRR:" + crr
    # body += "\n"+batsman1name+"\t"+batsman1score+"("
    toast.show_toast(title, body, duration=7)
    time.sleep(13)

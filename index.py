from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import excel_logic as ex
import calc_time as ct

ct.start_time

url = 'https://www.noxinfluencer.com/youtube-channel-rank/top-100-all-all-youtuber-sorted-by-subs-weekly'

driver = webdriver.Chrome()
driver.get(url)


def launchBrowser():
    wait = WebDriverWait(driver, 10)

    # ex.wb.save("sample.xlsx")
    ct.calc_total_time()

    while (True):
        pass


launchBrowser()

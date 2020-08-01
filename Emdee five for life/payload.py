#!/usr/bin/python3

import sys
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from hashlib import md5

def getMD5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()

def main(url):
    print("[+] Creating instance of Firefox..")
    DRIVER_PATH = '/usr/local/bin/geckodriver'
    BINARY_PATH = '/usr/bin/firefox-esr'
    HTB_URL = 'http://' + url

    ops = Options()
    ops.add_argument('--headless')
    ops.binary_location = BINARY_PATH
    serv = Service(DRIVER_PATH)
    browser = webdriver.Firefox(service=serv, options=ops)
    print('[+] Fetching ' + HTB_URL)
    browser.get(HTB_URL)
    string_to_be_encode = browser.find_element_by_css_selector('body h3').text
    md5encoded = getMD5(string_to_be_encode)
    print("[+] MD5 Encoded String: " + md5encoded)
    print("[+] Send MD5 string to input and submit")
    inputhtml = browser.find_element_by_css_selector('input[name="hash"]')
    inputhtml.send_keys(md5encoded)
    submithtml = browser.find_element_by_css_selector('input[type="submit"]')
    submithtml.click()
    flag = browser.find_element_by_css_selector('body p').text
    print("[+] Found flag: " + flag)

if __name__ == "__main__":
    main(sys.argv[1])
    
    
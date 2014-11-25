import mechanize
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import codecs
import getpass
driver = webdriver.Firefox()

USERNAME = str(raw_input("username: "))
PASSWORD = getpass.getpass("password: ")



def htmlHandle(USERNAME, PASSWORD):

    url = 'https://my.olin.edu/ICS/My_StAR/My_Schedule_and_Registration_Info.jnz'

    viewdetails = "pg0_V_lnkView"
    driver.get(url)
    elem = driver.find_element_by_name('userName')
    elem.send_keys(USERNAME)
    elem = driver.find_element_by_name('password')
    elem.send_keys(PASSWORD)

    driver.find_element_by_id("btnLogin").click()


    driver.find_element_by_id(viewdetails).click()
    html = driver.page_source

    soup = BeautifulSoup(html)
    return html

testfile =open('html.txt','w')

testfile.write(htmlHandle(USERNAME,PASSWORD))


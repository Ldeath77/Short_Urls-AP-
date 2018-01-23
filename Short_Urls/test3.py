import requests
import bs4
import pandas
import urllib
import numpy

from selenium import webdriver
from bs4 import BeautifulSoup

from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))
display.start()
#driver = webdriver.Chrome()


if __name__ == '__main__':
    link_to_scrape = "http://rlu.ru/1nvUT"
    print "Scrapping :: " + link_to_scrape
    driver = webdriver.Chrome('/usr/bin/chromedriver')
    driver.get(link_to_scrape)
    #page_being_scrape = requests.get(link_to_scrape)
    page_soup = bs4.BeautifulSoup(driver.page_source, "lxml")
    #table_data = page_soup.find_all('tr')
    #print table_data
    #print page_soup

    driver.quit()
    mal_url = page_soup.find_all('a',href=True)
    print mal_url
    '''for table in page_soup.find_all('table'):
        for subtable in table.find_all('td'):
            print subtable
        print "New Table"'''

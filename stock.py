#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 11:28:05 2021

@author: pao
"""

from bs4 import BeautifulSoup as bs 
from selenium import webdriver
import requests as rq
import csv
import time

def generate_urls(url, stock_nums):#generate the url of the page we want to scrapy
    urls = []

    for stock_num in stock_nums:
        urls.append(url + str(stock_num))
    return urls

def web_scraping_bot(urls):#scrapy all information of stocks I want
    stocks = [['開盤', '買價', '賣價', '成交', '單量', '總量', '昨量']]

    for url, stock_id in zip(urls, stock_ids):
        r = get_page_source(url)
        soup = parse_html(r)
        stock_inf = get_stock(soup)
        stocks.append(stock_inf)
    return stocks

def get_page_source(url):#request parameter url 
    global driver
    # headers = {
    #            'user-agent': 'Mozilla/5.0' 
    #            '(Macintosh Intel Mac OS X 10_13_4)' 
    #            'AppleWebKit/537.36 (KHTML, like Gecko)'
    #            'Chrome/66.0.3359.181 Safari/537.36'
    #           }
    driver.get(url)
    frame = driver.find_element_by_xpath('/html/body/center/table[1]/tbody/tr/td[1]/table[2]/tbody/tr/td/table/tbody/tr/td[1]/iframe')
    driver.switch_to.frame(frame)
    html = driver.page_source

    return html

def parse_html(text):#send back the soup object of parameter
    return bs(text, 'lxml')

def get_stock(soup):# get the information of stock
    inf = []
    flag = 0
    #  because all the tag all siblings with each other
    # so we just found the "oldest" tag and kept finding 
    # the next sibling in a loop which run seven times.   
    for i in range(0, 7):
        if flag == 0:
            tag = soup.select('svg > g:nth-child(35)')[0]
            inf.append(tag.text)
            flag += 1
        elif flag != 0:
            tag = tag.next_sibling
            inf.append(tag.text)

    return inf

def save_to_csv(data, file_name):#save our data to csv format
    with open(file_name + '.csv', 'w', encoding='utf-8') as fp:
        csv.writer(fp).writerows(data)

if __name__ == "__main__":
    driver = webdriver.Chrome("./chromedriver")
    driver.implicitly_wait(4)
    URL = "https://tw.stock.yahoo.com/q/bc?s="
    stock_ids = ["3711", "2330", "2454", "5287"]
    urls = generate_urls(URL, stock_ids)
    stocks = web_scraping_bot(urls)

    driver.quit()

    for stock in stocks:
        print(stock)
    save_to_csv(stocks, "stocks")


#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import ssl
import json
from urllib.request import Request, urlopen

# For ignoring SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
def ScrapeData(url):
    # Input from the user
    # Making the website believe that you are accessing it using a Mozilla browser
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    # Creating a BeautifulSoup object of the HTML page for easy extraction of data.

    soup = BeautifulSoup(webpage, 'html.parser')
    html = soup.prettify('utf-8')
    company_json = {}
    other_details = {}
    for div in soup.findAll('div', attrs={'class': 'D(ib) Mb(2px)'}):
        for h1 in div.findAll('h1', attrs={'class': 'D(ib) Fz(16px) Lh(18px)'},recursive=False):
            company_json['COMPANY NAME'] = h1.text.strip()
    for span in soup.findAll('span',
                            attrs={'class': 'Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)'
                            }):
        company_json['CURRENT PRICE'] = span.text.strip()
    for div in soup.findAll('div', attrs={'class': 'D(ib) Va(t)'}):
        for span in div.findAll('span', recursive=False):
            company_json['CURRENT GROWTH'] = span.text.strip()
    for td in soup.findAll('td', attrs={'data-test': 'PREV_CLOSE-value'}):
        for span in td.findAll('span', recursive=False):
            other_details['PREVIOUS CLOSE VALUE'] = span.text.strip()
    for td in soup.findAll('td', attrs={'data-test': 'OPEN-value'}):
        for span in td.findAll('span', recursive=False):
            other_details['OPEN'] = span.text.strip()
    for td in soup.findAll('td', attrs={'data-test': 'BID-value'}):
        for span in td.findAll('span', recursive=False):
            other_details['BID'] = span.text.strip()
    for td in soup.findAll('td', attrs={'data-test': 'ASK-value'}):
        for span in td.findAll('span', recursive=False):
            other_details['ASK'] = span.text.strip()
    for td in soup.findAll('td', attrs={'data-test': 'DAYS_RANGE-value'}):
        for span in td.findAll('span', recursive=False):
            other_details['DAYS RANGE'] = span.text.strip()
    for td in soup.findAll('td',
                        attrs={'data-test': 'FIFTY_TWO_WK_RANGE-value'}):
        for span in td.findAll('span', recursive=False):
            other_details['52 WEEK RANGE'] = span.text.strip()
    for td in soup.findAll('td', attrs={'data-test': 'TD_VOLUME-value'}):
        for span in td.findAll('span', recursive=False):
            other_details['TD VOL'] = span.text.strip()
    for td in soup.findAll('td',
                        attrs={'data-test': 'AVERAGE_VOLUME_3MONTH-value'
                        }):
        for span in td.findAll('span', recursive=False):
            other_details['AVG VOLUME 3 MONTHS'] = span.text.strip()
    for td in soup.findAll('td', attrs={'data-test': 'MARKET_CAP-value'}):
        for span in td.findAll('span', recursive=False):
            other_details['MARKET CAP'] = span.text.strip()
    for td in soup.findAll('td', attrs={'data-test': 'PE_RATIO-value'}):
        for span in td.findAll('span', recursive=False):
            other_details['PE RATIO'] = span.text.strip()
    for td in soup.findAll('td', attrs={'data-test': 'EPS_RATIO-value'}):
        for span in td.findAll('span', recursive=False):
            other_details['EPS RATIO'] = span.text.strip()
    for td in soup.findAll('td', attrs={'data-test': 'EARNINGS_DATE-value'
                        }):
        other_details['EARNINGS DATE'] = []
        for span in td.findAll('span', recursive=False):
            other_details['EARNINGS DATE'].append(span.text.strip())
    for td in soup.findAll('td',
                        attrs={'data-test': 'DIVIDEND_AND_YIELD-value'}):
        other_details['DIVIDEND & YIELD'] = td.text.strip()
    for td in soup.findAll('td',
                        attrs={'data-test': 'EX_DIVIDEND_DATE-value'}):
        for span in td.findAll('span', recursive=False):
            other_details['EX DIVIDEND DATE'] = span.text.strip()
    for td in soup.findAll('td',
                        attrs={'data-test': 'ONE_YEAR_TARGET_PRICE-value'
                        }):
        for span in td.findAll('span', recursive=False):
            other_details['ONE YR PREDICTION'] = span.text.strip()
    company_json['OTHER_DETAILS'] = other_details
    with open('COMMODITY_DATA.json', 'w') as outfile:
        json.dump(company_json, outfile, indent=4)
    print (company_json)
    with open('output_file.html', 'wb') as file:
        file.write(html)
    print ('----------Extraction is complete. Data saved in your folder.----------')

    return company_json

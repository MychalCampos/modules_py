# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 19:59:15 2018

# scrape a single data series from the web using BeautifulSoup
# and return to a list

@author: Mychal
"""

from bs4 import BeautifulSoup

def get_soup_data(soup, soup_select):
    
    # inputs:
    # @param soup is a BeautifulSoup object, e.g.,
    # soup = BeautifulSoup(html_file, 'lxml')
    # @param soup_select is the div class that contains specific text, e.g.,
    # soup_select = soup.select('div[class*="cell-col-2 ag-cell-value rating-"]')
    
    # output:
    # @param the_data = the desired data series in a list  
    
    the_data = []
    for d in soup.select(soup_select):
        the_data.append(d.get_text())
    return the_data
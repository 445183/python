from selenium import webdriver
from bs4 import BeautifulSoup
import csv,time

URL="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser=webdriver.Chrome("chromedriver.exe")
browser.get(URL)
time.sleep(10)

headers=["V mag.","Proper Name","Bayer designation","Distance","Spectral class","Mass","Radius","Luminosity"]

def Scrape_data():
    soup=BeautifulSoup(browser.page_source,'html.parser')
    star_data=[]
    temp_list=[]
    for i in range(1,98):
        for tr_tag in soup.find_all('tr'):
            td_tags=tr_tag.find_all('td')

            for index,td_tag in enumerate(td_tags):
                try:
                    if td_tag.contents[2]:
                        temp_list.append(td_tag.contents[2])
                except:
                    try:
                        if td_tag.contents[1] and index==1:
                            temp_list.append(td_tag.find('a').contents[0])
                        else:
                            temp_list.append(td_tag.contents[1])
                    except:
                        if td_tag.contents[0]:
                            temp_list.append(td_tag.contents[0]) 
    star_data.append(temp_list) 
    print(star_data)
    
    with open("starData.csv", "w") as f:
        csvwriter=csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(star_data)
Scrape_data()
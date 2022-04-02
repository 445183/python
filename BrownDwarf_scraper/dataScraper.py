from bs4 import BeautifulSoup
from selenium import webdriver
import csv,time

URL="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser=webdriver.Chrome('chromedriver.exe')
browser.get(URL)

time.sleep(5)

headers=["Star","Constellation","Right ascension","Declination","App. mag.","Distance (ly)","Spectral type","Brown dwarf"]
final_data=[]

def scrapeData():
    soup=BeautifulSoup(browser.page_source,'html.parser')
    table_tags=soup.find_all('table',attrs={'class','wikitable sortable jquery-tablesorter'})

    for table_tag in table_tags:
        tbody_tags=table_tag.find_all('tbody')
        for tbody_tag in tbody_tags :
            tr_tags=tbody_tag.find_all('tr')
            for tr_tag in tr_tags:
                td_tags=tr_tag.find_all('td')
                
                columns=[]
                for index,td_tag in enumerate(td_tags):
                    column=td_tag
                    column_no=index

                    if column_no==0 or column_no==1 or column_no==3 or column_no==4 or column_no==5 or column_no==6:
                        try:
                            data=column.find('a').contents[0]
                            columns.append(data)
                        except:
                            try:
                                data=column.contents[0]
                                columns.append(data)
                            except:
                                columns.append("-")

                    elif column_no==2:
                        try:
                            span_tag=column.find('span')
                            try :
                                if span_tag.contents[4]:
                                    p1=span_tag.contents[0]
                                    sup1=span_tag.contents[1].contents[0]
                                    p2=span_tag.contents[2]
                                    sup2=span_tag.contents[3].contents[0]
                                    p3=span_tag.contents[4]
                                    sup3=span_tag.contents[5].contents[0]
                                    data=p1+sup1+p2+sup2+p3+sup3
                                    columns.append(data)
                            except:
                                p1=span_tag.contents[0]
                                sup1=span_tag.contents[1].contents[0]
                                p2=span_tag.contents[2]
                                sup2=span_tag.contents[3].contents[0]
                                data=p1+sup1+p2+sup2
                                columns.append(data)
                        except:
                            columns.append("-")
                    
                    elif column_no==7:
                        try:
                            try:
                                data=int(column.contents[0])  
                            except:
                                try:
                                    data=column.contents[0].contents[0]
                                except:
                                    data=column.contents[0]
                                columns.append(data)
                        except:
                            columns.append("-")    
                final_data.append(columns)

def CSV_fileMaker(p1,p2):
    with open('brown_dwarfs.csv', 'w', newline='',encoding="utf-8") as f:
        file=csv.writer(f)
        file.writerow(p1)
        file.writerows(p2)

        print(p2)

scrapeData()
CSV_fileMaker(headers,final_data)
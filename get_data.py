import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import openpyxl
import re

ILLEGAL_CHARACTERS_RE = re.compile(r'[\000-\010]|[\013-\014]|[\016-\037]')

#settings
scroll_time = 500
driver = webdriver.Chrome()
url = "https://udn.com/news/breaknews/1/99#breaknews"
driver.get(url)


#模擬網頁滾動事件
for i in range(1, scroll_time+1):
    time.sleep(3) #延遲執行時間
    print(f"now scroll {i}/{scroll_time}")
    js = "window.scrollTo(0, document.body.scrollHeight);"
    driver.execute_script(js)

#抓取html資料
time.sleep(3) #延遲執行時間
r = driver.page_source
soup = BeautifulSoup(r,"html.parser")
head = soup.select("div.story-list__text > h2 > a")
print("article number =", len(head))
print("-------------------")

#counting settings
count = 0
i = count + 1

#output in excel
workbook = openpyxl.Workbook()
worksheet = workbook.active

#抓取分頁資料，並存入excel中
for h in head: 
    count += 1
    print("on the process of ",count)
    #進入內文+爬取url
    url = "https://udn.com" + h["href"] #url更新為內文的網址
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")
    #爬取內文
    find_article = soup.select("section.article-content__editor p")
    tmp = ''
    for d in find_article:
        tmp = tmp + d.text + "\n"
    print("appending article")
    text = ILLEGAL_CHARACTERS_RE.sub(r'',tmp)
    worksheet.cell(row = i,column = 6,value = text) # j = 6 means article
    # print("內文 : ",i.text)
    tmp = None 
    print("-------------------")
    workbook.save("output.xlsx")
    i += 1
    
print("repti finished")
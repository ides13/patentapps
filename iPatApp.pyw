# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 09:13:47 2019

@author: ides13
"""

from tkinter import *
from tkinter.ttk import Button 
from tkinter.filedialog import askdirectory
import os
import requests
import bs4
import time
import re

def _open():
    #SaveDirectory = os.getcwd() #印出目前工作目錄
    #取得目前python scripts的路徑
    pathname = os.path.dirname(sys.argv[0])        
    SaveDirectory  = os.path.abspath(pathname)
    #print(SaveDirectory)
    datas = retrieve_input(t_start)
    
    with open(os.path.join(SaveDirectory,'datafile.txt'), 'w', encoding = 'utf-8') as F:
        F.write(datas)
    os.system(os.path.join(SaveDirectory,'prefnum.exe')) 
    
    with open(os.path.join(SaveDirectory,'workfile.txt'), 'r', encoding = 'utf-8') as F:
        string = F.read()
    set_input(t_end, string + os.path.join(SaveDirectory,'workfile.txt'))
    return

def savePats():
    datas = retrieve_input(t_start)
#    print(datas)
    pats= datas.split('\n')
    downloadpats(pats)
    set_input(t_end, "下載完畢")
    return

def add_signature():
    
    return

def add_date():
    
    return

def retrieve_input(textBox):
    inputValue=textBox.get("1.0","end-1c")
#    print(inputValue)
    return inputValue

def set_input(textBox, value):
    textBox.delete(1.0, END)
    textBox.insert(END, value)
#    print(inputValue)
    return

#============================================================================================
rooturl='https://patents.google.com/patent/{}'
headers = ('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36')
waittime = 5

#=====================================================

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import re


# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# #chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--headless")
# #driver = webdriver.Chrome(chrome_options=chrome_options)

# class TestWww():
#   def __init__(self, num):
#     self.driver = webdriver.Chrome(chrome_options=chrome_options)
#     self.vars = {}
#     self.num = num
#     self.url =""
#     self.patentnumber = ""
#     self.test_www()
  
#   def teardown_method(self, method):
#     self.driver.quit()
  
#   def test_www(self):
#     self.driver.get("https://patents.google.com/")
#     self.driver.set_window_size(1278, 824)
#     self.driver.find_element(By.ID, "searchInput").click()
#     self.driver.find_element(By.ID, "searchInput").send_keys(self.num)
#     self.driver.find_element(By.CSS_SELECTOR, "#searchButton > .style-scope").click()
#     self.url = self.driver.current_url
# #    print(self.url)
#     self.patentnumber = re.search(".*/patent/(.*)/.*", self.url).group(1)

# #=====================================================

# def getfile_test(name, temp):
#     '''
#     temp = requests.get(ufl, stream=True)
#     輸入一個「requests.get」後的物件。
#     '''
#     with open(name, 'wb') as f:
#         f.write(temp.content)
#     return


# def getfile(name, temp):
#     '''
#     temp = requests.get(ufl, stream=True)
#     輸入一個「requests.get」後的物件。
#     '''
#     x = re.search("\w+.*?", name)
#     foldername = x.group(0)
#     path = "\\"+foldername
#     if not os.path.isdir(path):
#         os.mkdir(path)
# 	#file = open(path + "\\" + "我要開檔案.txt", "w")
#     with open(path + "\\" +name, 'wb') as f:
#         f.write(temp.content)
#     return

# def uspatent_download(patnum):
#     #下載 html 檔
#     USPatentUrl = rooturl.format(patnum)
#     response = requests.get(USPatentUrl, stream=True)
# 	
#     namehtml = '{}.html'.format(patnum)     #print(namehtml)
#     getfile(namehtml, response)
    
#     #下載 pdf 檔，需先取得pdf網址「pdfLink」
#     html = response.text
#     soup = bs4.BeautifulSoup(html,'html.parser')
#     pdfLink = soup.find("a", {"itemprop":"pdfLink"}).attrs["href"]
#     time.sleep(waittime)
#     pdfLinktemp = requests.get(pdfLink, stream=True)

#     namepdf = '{}.pdf'.format(patnum)       #print(namepdf, pdfLink)
#     getfile(namepdf, pdfLinktemp)
#     return

# def  downloadpats(pats):
#     for pat in pats:
#         patnum = TestWww(pat).patentnumber
#         time.sleep(waittime)
#         uspatent_download(patnum)
#     return

#====================================================================


root = Tk()
#button = Button(root, text = 'Geeks') 
#button.pack(side = TOP, pady = 5) 


menubar = Menu(root)
menubar.add_command(label="元件符號", command=_open)
menubar.add_command(label="下載專利", command=savePats)
menubar.add_command(label="Add signature",command=add_signature)
menubar.add_command(label="Add date",command=add_date)
root.config(menu=menubar)



left = Frame(root)
right = Frame(root)

t_start = Text(left)
t_start.pack(side=LEFT, fill=Y)
s_start = Scrollbar(left)
s_start.pack(side=RIGHT, fill=Y)
s_start.config(command=t_start.yview)
t_start.config(yscrollcommand=s_start.set)

t_end = Text(right)
t_end.pack(side=LEFT, fill=Y)
s_end = Scrollbar(right)
s_end.pack(side=RIGHT, fill=Y)
s_end.config(command=t_end.yview)
t_end.config(yscrollcommand=s_end.set)

left.pack(side=LEFT, fill=Y)
right.pack(side=RIGHT, fill=Y)

root.geometry("1100x700")
root.mainloop()

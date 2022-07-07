import webbrowser
import os
import psutil
from googlesearch import search
import urllib
from bs4 import BeautifulSoup

#config for test
web_page = 'https://github.com/DashaDAC'
app_page = "/snap/bin/atom"
num = 1
num_stop=1
query = "hackernoon How To Scrape Google With Python"
web_flag=2

print(os.path.basename(app_page))

def web_open(web_page, web_flag):
    webbrowser.open(web_page, new=web_flag)

def app_open(app_page):
    os.system(app_page)

def app_kill(app_page):
    name_app = os.path.basename(app_page)
    for process in (process for process in psutil.process_iter() if process.name() == name_app):
        process.kill()

def google_search(query, num, num_stop, flag):
    for search_page in search(query, num=num, stop=num_stop):
        # print(search_page)
        web_open(search_page, flag)
    return search_page

#test
app_kill(app_page)
search_page = google_search(query, num, num_stop, 2)
print(search_page)
web_open(web_page, 2)

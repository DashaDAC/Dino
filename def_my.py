import webbrowser
import os
import psutil

web_page = 'https://github.com/DashaDAC'
app_page = "/snap/bin/atom"
app_page = "atom"
print(os.path.expandvars(app_page))

def web_open(web_page):
    webbrowser.open(web_page, new=2)

def app_open(app_page):
    os.system(app_page)

def app_kill(app_page):
    name_app = os.path.expandvars(app_page)
    for process in (process for process in psutil.process_iter() if process.name() == name_app):
        process.kill()
#test
app_open(app_page)
web_open(web_page)

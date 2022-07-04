import webbrowser
web_page = 'https://github.com/DashaDAC'

def web_open(web_page):
    webbrowser.open(str(web_page), new=2)

web_open(web_page)
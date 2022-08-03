import mechanicalsoup

def get_scrape_url():
    url = input("Please insert url :")
    return url

def get_page(url):
    browser = mechanicalsoup.Browser()
    login_page = browser.get(url)
    return login_page
import mechanicalsoup

def get_scrape_url():
    url = input("Please insert url :")
    return url

def get_page(url):
    browser = mechanicalsoup.Browser()
    login_page = browser.get(url)
    return login_page

def parse_page_as_html(page):
    parse_page = page.soup
    return parse_page

def login(form, login_page_url):
    browser = mechanicalsoup.Browser()
    form.select("input")[0]["value"] = input("Please insert username :")
    form.select("input")[1]["value"] = input("Please insert password :")
    profiles_page = browser.submit(form, login_page_url)
    return profiles_page

def get_a_element(page, base_url):
    for link in page.soup.find_all("a"):
        link_url = {}
        link_url[link.text] = base_url + link["href"]
    return link_url

def result(page, links):
    print(f"Title : {page.soup.title.text}, {links}")

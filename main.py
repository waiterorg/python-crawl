import mechanicalsoup

browser = mechanicalsoup.Browser()

login_url = "http://olympus.realpython.org/login"
login_page = browser.get(login_url)
login_html = login_page.soup
base_url = "http://olympus.realpython.org"

form = login_html.form
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

profiles_page = browser.submit(form, login_page.url)

print(f"Title : {profiles_page.soup.title.text}")

for link in profiles_page.soup.find_all("a"):
    link_url = {}
    link_url[link.text] = base_url + link["href"]
    print(f"{link.text} : {link_url[link.text]} \n")
    

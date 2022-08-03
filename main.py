from utils import scrape

def get_profile_page():    
    url = scrape.get_scrape_url()
    page = scrape.get_page(url)
    parse_page = scrape.parse_page_as_html(page)
    profile_page = scrape.login(parse_page.form, page.url)
    links = scrape.get_a_element(profile_page, url.rsplit('/', 0)[0])
    result = scrape.result(profile_page, links)
    return result

get_profile_page()
from requests_html import HTMLSession
from bs4 import BeautifulSoup

if __name__ == '__main__':

    session = HTMLSession()
    r = session.get("https://explorer.kaspa.org/")
    r.html.render(sleep=2, keep_page=True, scrolldown=0)
    soup = BeautifulSoup(r.html.raw_html, "html.parser")
    print(soup)
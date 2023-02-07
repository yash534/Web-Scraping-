#importing beautifulSoup library for scrapping.
from bs4 import BeautifulSoup
#importing requests library for sending request to url for getting imformation from their website.
import requests

#sending request to website.
html_text = requests.get('https://en.wikipedia.org/wiki/AliExpress').text
#using lxml parser for parsing.
soup = BeautifulSoup(html_text, 'lxml')

#scrapping data using class of that element that are available on this url.
heading = soup.find_all('span', class_ = 'mw-page-title-main')
sidebar_links = soup.find('li', class_ = 'mw-list-item').text.replace(' ','')
headline = soup.find_all('span', class_ = 'mw-headline')

#scraping all the href elements present in the given url.
urls = []
for link in soup.find_all('a'):
    print(link.get('href'))
    
print(f'''
Headings:: {heading}
Sidebar Links:: {sidebar_links}
Headline:: {headline}
''')








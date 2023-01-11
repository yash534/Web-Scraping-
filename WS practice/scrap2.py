#importing beautifulSoup library for scrapping.
from bs4 import BeautifulSoup
#importing requests library for sending request to url for getting imformation from their website.
import requests

#sending request to website.
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
#using lxml parser for parsing.
soup = BeautifulSoup(html_text, 'lxml')

#scrapping data using class of that element that are available on this url.
job = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
company_name = soup.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
skills = soup.find('span', class_ = 'srp-skills').text.replace(' ','')
published_date = soup.find('span', class_ = 'sin-posted').span.text


#finally printing the scrapped data.
print(f'''
Company Name:: {company_name}
Required Skills:: {skills}
Published Date:: {published_date}
''')



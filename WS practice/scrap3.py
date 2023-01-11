from bs4 import BeautifulSoup
import requests

#sending request to website.
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
#using lxml parser for parsing.
soup = BeautifulSoup(html_text, 'lxml')

#scrapping data using class of that element that are available on this url.
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

for job in jobs:
    published_date = job.find('span', class_='sin-posted').span.text
    if 'few' in published_date:
        company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
        skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
        more_info = job.header.h2.a

        print(f"Company Name: {company_name.strip()}" )
        print(f"Required skills:  {company_name.strip()}")
        print(f"Company Name:  {company_name.strip()}")

        print('')

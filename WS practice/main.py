from bs4 import BeautifulSoup

with open ('home.html', 'r') as html_file:
    content = html_file.read()
    

    soup = BeautifulSoup(content, 'lxml')
    tag = soup.find_all('h1')
    print(tag)
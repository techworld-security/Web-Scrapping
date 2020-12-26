import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract(page): 
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    URL = f'https://in.indeed.com/jobs?q=python+developer&l=Mumbai%2C+Maharashtra&start={page}'
    request = requests.get(URL, headers)
    soup = BeautifulSoup(request.content, 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('div', class_ = 'jobsearch-SerpJobCard')
    for item in divs:
        title = item.find('a').text.strip()
        try:
            salary = item.find('span', class_ = 'salaryText').text.strip()
        except:
            salary = ''
        company = item.find('span', class_ = 'company').text.strip()
        summary = item.find('div', class_ = 'summary').text.strip()
        job = {
            'title' : title,
            'salary' : salary,
            'company' : company,
            'summary' : summary,
        }
        joblist.append(job)
    return

joblist = []
for i in range(0,100,10):
    print (f'looking in page,{i}')
    c = (extract(0))
    transform(c)
df = pd.DataFrame(joblist)
print(df.head())
df.to_excel("Mumbaijobs.xlsx")

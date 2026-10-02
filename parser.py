import requests
from bs4 import BeautifulSoup

URL = "https://jobs.dou.ua/vacancies/?category=Python&exp=0-1"
HEADERS = {"User-Agent": "Mozilla/5.0"}

response = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(response.text, "html.parser")

for vacancy in soup.select("li.l-vacancy"):
    title = vacancy.select_one("a.vt")
    company = vacancy.select_one("a.company")
    print(title.text.strip(), "|", company.text.strip(), "|", title["href"])

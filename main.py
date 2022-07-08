import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/Users/Sarge/Downloads/chromedriver_win32/chromedriver.exe')
driver.get('https://oxylabs.io/blog')
results = []
other_results = []
content = driver.page_source
soup = BeautifulSoup(content)
driver.quit()

for a in soup.findAll(attrs='class=css-y23utb e19fcc3m0'):
    name = a.find('h4')
    if name not in results:
        results.append(name.text)

for b in soup.findAll(attrs='class=css-un9815 e15x7lld1'):
    date = b.find('p')
    if date not in results:
        other_results.append(date.text)

df = pd.DataFrame({"Names": results, "Dates": other_results})
df.to_csv('names.csv', index=False, encoding='utf-8')

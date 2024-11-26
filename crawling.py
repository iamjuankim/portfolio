import requests
from bs4 import BeautifulSoup

titles = []
search_word = '고려대학교'
url = f'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query={search_word}'
req = requests.get(url)
html = req.text
#print(html)

soup = BeautifulSoup(html, 'html.parser')
search_result = soup.select_one('.list_news')
news_links = search_result.select('.bx > .news_wrap > .news_area > .news_contents > .news_tit')
for i in news_links:
  titles.append(i.get_text())
#print(titles)

print(titles)
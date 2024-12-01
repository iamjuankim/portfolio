from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import requests
from bs4 import BeautifulSoup

#크롤링
titles = []
search_word = '크리스마스'
url = f'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query={search_word}'
#print(url)
req = requests.get(url)
html = req.text
#print(html)

soup = BeautifulSoup(html, 'html.parser')
search_result = soup.select_one('.list_news')
news_links = search_result.select('.bx > .news_wrap > .news_area > .news_contents > .news_tit')
#print(news_links)
for i in news_links:
  titles.append(i.get_text())
#print(titles)


#워드클라우드

a = ''
#리스트의 내용 한 줄로 추출

for x in titles:
    a = a + x
#print(a)

img = Image.open("C:\\Users\\Juan Kim\\Downloads\\tree.png")
img_array = np.array(img)

wordcloud = WordCloud(font_path="C:\\Users\\Juan Kim\\Downloads\\NanumGothicExtraBold.ttf", width=800, height=800, background_color="white", mask=img_array)
wordcloud = wordcloud.generate(a)

plt.figure()
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
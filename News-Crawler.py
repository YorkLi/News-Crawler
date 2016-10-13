# coding=utf-8

import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.google.com")
soup = BeautifulSoup(res.text,"lxml")

#HOT news

hot_news=soup.select(".section.top-stories-section.section-toptop")[0]
hot_news_title = hot_news.select(".section-name")[0].text
print('======['+hot_news_title+']=========')
for i in range(len(hot_news.select(".esc-lead-article-title"))):
	news_title = hot_news.select(".esc-lead-article-title")[i].text
	news_url = hot_news.select(".esc-lead-article-title")[i].find('a')['href']
	news_source = hot_news.select(".al-attribution-source")[i].text
	news_timestamp = hot_news.select(".al-attribution-timestamp")[i].text
	print(news_title)
	print(news_url)
	print(news_source+" , "+news_timestamp)

category = ["w","n","b","t","s","e","c","y","m"] #Google news category

for i in category :
	news_category=soup.select(".section.story-section.section-zh-TW_tw-"+i)[0]
	news_category_title = news_category.select(".section-name")[0].text

	print('======['+news_category_title+']=========')

	for j in range(len(news_category.select(".esc-lead-article-title"))):
		news_title = news_category.select(".esc-lead-article-title")[j].text
		news_url = news_category.select(".esc-lead-article-title")[j].find('a')['href']
		news_source = news_category.select(".al-attribution-source")[j].text
		news_timestamp = news_category.select(".al-attribution-timestamp")[j].text
		print(news_title)
		print(news_url)
		print(news_source+" , "+news_timestamp)

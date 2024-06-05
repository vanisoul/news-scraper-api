import requests
from bs4 import BeautifulSoup

def scrape_news():
    url = 'https://www.techbang.com/categories/69'
    response = requests.get(url)
    response.encoding = 'utf-8'  # 設定編碼

    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # 查找所有符合條件的 <a> 標籤
    articles = soup.find_all('article', class_='article brief-post')

    # 初始化結果陣列
    result = []

    # 迭代每個 article 元素，提取 title 和 link 屬性
    for article in articles:
        a_tag = article.find('h2', class_='post-title').find('a')
        title = a_tag['title']
        link = a_tag['href']
        result.append({'title': title, 'link': link})


    # 輸出結果
    for item in result:
        print(f"Title: {item['title']}, Link: {item['link']}")

    return result

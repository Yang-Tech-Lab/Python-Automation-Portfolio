import requests
import pandas as pd
from bs4 import BeautifulSoup

print("1. 正在连接目标网站...")
url = "http://books.toscrape.com/"
response = requests.get(url)

if response.status_code == 200:
    print("✅ 连接成功！开始抓取数据...")
    soup = BeautifulSoup(response.text, "html.parser")
    all_books = soup.find_all("article", class_="product_pod")
    
    # 创建一个空列表，用来装我们抓到的数据
    book_list = []
    
    for book in all_books:
        title = book.h3.a["title"]
        # 这里的 replace 是为了把那个奇怪的乱码符号去掉
        price = book.find("p", class_="price_color").text.replace('Â', '')
        
        # 把这本书的信息，打包成一个字典，装进列表里
        book_list.append({
            '书名': title,
            '价格': price
        })
        print(f"已捕获: {title}")

    print("-" * 30)
    print("2. 正在保存到 Excel...")
    
    # 把列表转换成表格
    df = pd.DataFrame(book_list)
    
    # 保存文件
    df.to_excel('fiverr_books.xlsx', index=False)
    
    print("🎉 大功告成！文件 [fiverr_books.xlsx] 已保存！")

else:
    print("❌ 连接失败")
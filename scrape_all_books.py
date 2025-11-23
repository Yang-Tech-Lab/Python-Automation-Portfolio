import requests
import pandas as pd
from bs4 import BeautifulSoup
import time # 引入时间库，用来模拟休息

print("🚀 启动超级爬虫！准备抓取前 5 页的数据...")

# 创建一个大列表，用来装所有页面的书
all_books_data = []

# 循环 1 到 5 页 (range(1, 6) 意思是从1开始，到6结束，不包含6)
# 如果你想抓 50 页，就把 6 改成 51
for page_num in range(1, 6):
    print(f"正在抓取第 {page_num} 页...")
    
    # 构造每一页的网址 (注意 f-string 的用法)
    url = f"http://books.toscrape.com/catalogue/page-{page_num}.html"
    
    # 发送请求
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        books_on_page = soup.find_all("article", class_="product_pod")
        
        # 遍历这一页的每一本书
        for book in books_on_page:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text.replace('Â', '')
            
            # 存入大列表
            all_books_data.append({
                '页码': page_num,  # 记录一下是哪一页抓的
                '书名': title,
                '价格': price
            })
    else:
        print(f"⚠️ 第 {page_num} 页连接失败！")
    
    # 【防封号关键】每抓完一页，休息 1 秒
    # 告诉网站：我是人，我不是机器，我手速没那么快
    time.sleep(1)

print("-" * 30)
print(f"✅ 抓取结束！总共抓到了 {len(all_books_data)} 本书。")
print("正在保存到 Excel...")

# 保存文件
df = pd.DataFrame(all_books_data)
df.to_excel('fiverr_books_all.xlsx', index=False)

print("🎉 文件 [fiverr_books_all.xlsx] 已生成！")
import pandas as pd
import random
from datetime import datetime, timedelta

print("🎰 市场模拟器启动...")

# 模拟 5 个竞争对手的产品
products = ["Gaming Mouse", "Mechanical Keyboard", "USB-C Hub", "Webcam 4K", "Monitor Stand"]
base_prices = [50, 80, 30, 120, 40] # 基础价格

data = []

# 生成过去 7 天的数据
for i in range(7):
    date = (datetime.now() - timedelta(days=6-i)).strftime("%Y-%m-%d")
    
    for prod, base in zip(products, base_prices):
        # 价格在基础价格上下波动 10%
        fluctuation = random.uniform(0.9, 1.1) 
        price = round(base * fluctuation, 2)
        
        data.append({
            "Date": date,
            "Product": prod,
            "Competitor_Price": price,
            "My_Cost": base * 0.6 # 假设我的成本是售价的 60%
        })

df = pd.DataFrame(data)
csv_file = "competitor_data.csv"
df.to_csv(csv_file, index=False)

print(f"✅ 市场数据已刷新！已生成 [{csv_file}]")
print("（提示：你可以多运行几次这个脚本，模拟不同的市场行情）")
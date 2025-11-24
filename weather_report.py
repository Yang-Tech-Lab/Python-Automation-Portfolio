import requests
import pandas as pd
from datetime import datetime
import time

print("🚀 批量天气报表生成器启动...")

# 1. 你的万能钥匙
api_key = "103104f0c64435943e54807674a02704"
base_url = "http://api.openweathermap.org/data/2.5/weather"

# 2. 客户指定的城市列表
cities = ["Beijing", "Shanghai", "Tokyo", "New York", "London", "Paris", "Berlin"]

# 准备一个空列表装数据
weather_data = []

print("-" * 30)

# 3. 开始循环抓取
for city in cities:
    print(f"📡 正在查询: {city}...")
    
    try:
        # 拼接 URL
        url = f"{base_url}?q={city}&appid={api_key}&units=metric&lang=zh_cn"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            
            # 提取数据
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            humidity = data['main']['humidity']
            
            print(f"   ✅ {temp}°C | {desc}")
            
            # 存入列表
            weather_data.append({
                "城市": city,
                "温度 (°C)": temp,
                "天气状况": desc,
                "湿度 (%)": humidity,
                "更新时间": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
        else:
            print(f"   ❌ 获取失败")
            
    except Exception as e:
        print(f"   ❌ 网络错误: {e}")
    
    # 稍微停顿一下，防止请求太快
    time.sleep(0.5)

# 4. 保存到 Excel
print("-" * 30)
print("💾 正在保存报表...")

if weather_data:
    df = pd.DataFrame(weather_data)
    file_name = "global_weather_report.xlsx"
    df.to_excel(file_name, index=False)
    print(f"🎉 成功！报表已生成: [{file_name}]")
    print("快去 D 盘看看你的战利品！")
else:
    print("⚠️ 没有抓取到任何数据。")
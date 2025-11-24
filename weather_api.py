import requests
import time

print("🌤️ 全球天气实时查询终端启动...")
print("--------------------------------")

# 1. 配置身份信息
# 这是你下午申请的那串“万能钥匙”，我帮你填好了
api_key = "103104f0c64435943e54807674a02704"
base_url = "http://api.openweathermap.org/data/2.5/weather"

while True:
    # 2. 输入城市
    city = input("\n🌍 请输入城市拼音 (例如 Beijing, London, 输入 q 退出): ").strip()
    
    if city.lower() == 'q':
        print("👋 系统关闭。")
        break

    # 3. 拼接“暗号” (URL)
    # units=metric 表示我们要看摄氏度，而不是开尔文
    # lang=zh_cn 表示我们要看中文的天气描述
    complete_url = f"{base_url}?q={city}&appid={api_key}&units=metric&lang=zh_cn"

    try:
        print("📡 正在连接卫星获取数据...")
        
        # 4. 发送请求 (这一步就是 Python 替你去服务器拿数据)
        response = requests.get(complete_url)
        
        # 5. 解析数据 (JSON)
        # 这一步是核心：把服务器返回的一堆乱码，变成 Python 字典
        data = response.json()

        # 检查状态码 (200 代表成功)
        if response.status_code == 200:
            # 提取我们关心的信息
            temp = data['main']['temp']        # 温度
            humidity = data['main']['humidity'] # 湿度
            desc = data['weather'][0]['description'] # 天气状况
            wind = data['wind']['speed']       # 风速
            name = data['name']                # 城市正式名称

            # 6. 打印漂亮的结果
            print(f"\n✅ 查询成功：【{name}】")
            print(f"🌡️  温度: {temp}°C")
            print(f"☁️  天气: {desc}")
            print(f"💧  湿度: {humidity}%")
            print(f"🌬️  风速: {wind} m/s")
        else:
            # 如果查不到 (比如输错了拼音)
            print("❌ 找不到这个城市，请检查拼音是否正确！")

    except Exception as e:
        print(f"❌ 网络连接错误: {e}")
        print("提示：如果一直报错，请检查是否开启了梯子 (OpenWeatherMap 国内有时候访问慢)")
import schedule
import time
import pandas as pd
from datetime import datetime
import os
import random  # 引入随机库，用来生成仿真数据

print("🛡️ 价格哨兵系统启动 (仿真测试模式)...")
print("正在初始化监控列表...")

# --- 1. 配置区域 (Configuration) ---
TARGET_ASSET = "BTC-USD"  # 监控目标
ALERT_PRICE = 98000       # 报警阈值：如果低于 $98,000 就报警
LOG_FILE = "price_monitor_log.csv"

# --- 2. 核心功能函数 ---

def get_current_price(ticker):
    """
    【仿真模式】
    由于网络原因连接不上雅虎财经，我们这里模拟真实的市场波动。
    价格会在 95,000 到 100,000 之间随机跳动。
    """
    # 模拟一个价格
    simulated_price = random.uniform(95000, 100000)
    return simulated_price

def save_log(price):
    """Record data to CSV (English Version)"""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    new_data = pd.DataFrame([{
        "Timestamp": now,              # 时间 -> Timestamp
        "Asset": TARGET_ASSET,         # 资产 -> Asset
        "Price ($)": f"{price:.2f}",   # 当前价格 -> Price
        # 状态 -> Status (正常 -> OK, 报警 -> ALERT)
        "Status": "OK" if price > ALERT_PRICE else "⚠️ ALERT"
    }])
    
    # 依然保留 utf-8-sig，因为我们要支持 emoji (⚠️)
    new_data.to_csv(LOG_FILE, mode='a', header=not os.path.exists(LOG_FILE), index=False, encoding='utf-8-sig')
    
    # 追加写入文件 (带上了防乱码神器 utf-8-sig)
    new_data.to_csv(LOG_FILE, mode='a', header=not os.path.exists(LOG_FILE), index=False, encoding='utf-8-sig')

def send_alert(price):
    """Send Alert (English Version with Red Color)"""
    RED = "\033[91m"
    RESET = "\033[0m"
    
    print("\n" + RED + "!"*50)
    print(f"🚨 URGENT ALERT! {TARGET_ASSET} Price Drop!") # 紧急警报
    print(f"📉 Current Price: ${price:,.2f}")             # 当前价格
    print(f"🛑 Threshold: ${ALERT_PRICE:,.2f}")          # 设定阈值
    print(f"📧 (Simulated) Email sent to Admin: Buy the dip!") # 发送邮件
    print("!"*50 + RESET + "\n")

# --- 3. 任务主逻辑 (Job) ---
def job():
    print(f"⏳ [{datetime.now().strftime('%H:%M:%S')}] 正在巡逻...", end="")
    
    price = get_current_price(TARGET_ASSET)
    
    # 显示价格
    print(f" 当前 {TARGET_ASSET}: ${price:,.2f}", end="")
    
    # 记录日志
    save_log(price)
    
    # 判断是否报警
    if price < ALERT_PRICE:
        send_alert(price)
    else:
        print(" -> ✅ 价格安全")

# --- 4. 设定定时任务 ---
# 为了演示效果，我们把速度调快：每 3 秒查一次
schedule.every(3).seconds.do(job)

print(f"✅ 监控已部署。目标: {TARGET_ASSET} | 阈值: < ${ALERT_PRICE}")
print("👉 请观察：当价格随机跌破 98000 时，系统会报警！")
print("按 Ctrl + C 可以强制停止系统。")
print("-" * 40)

# --- 5. 死循环引擎 ---
while True:
    schedule.run_pending()
    time.sleep(1)
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

print("🚀 机器人正在启动...")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

print("✅ 正在访问 Bing...")
driver.get("https://cn.bing.com")
time.sleep(3)

try:
    print("👀 寻找搜索框...")
    search_box = driver.find_element(By.ID, "sb_form_q")
    search_box.click()
    
    print("🤖 自动输入中...")
    search_box.send_keys("Fiverr")
    time.sleep(1)
    search_box.send_keys(Keys.RETURN)
    
    print("⏳ 等待搜索结果加载 (3秒)...")
    time.sleep(3)
    
    # 【新增功能】截图保存！
    # 这就是发给客户的“证据”
    print("📸 正在截图...")
    driver.save_screenshot('fiverr_search_result.png')
    print("✅ 截图已保存！")

except Exception as e:
    print(f"❌ 出错: {e}")

print("测试结束，5秒后关闭...")
time.sleep(5)
driver.quit()
import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import os
from datetime import datetime

print("🧠 商业情报系统正在初始化...")

# 1. 读取市场数据
try:
    df = pd.read_csv("competitor_data.csv")
    print("✅ 成功加载市场数据。")
except:
    print("❌ 找不到数据！请先运行 market_simulator.py")
    exit()

# 准备 PDF 文件名
report_name = f"Strategy_Report_{datetime.now().strftime('%Y%m%d')}.pdf"
c = canvas.Canvas(report_name, pagesize=letter)
width, height = letter # 获取页面宽高

# --- PDF 排版开始 ---

# A. 写入标题头
c.setFont("Helvetica-Bold", 24)
c.drawString(50, 750, "Daily Competitor Intelligence Report")
c.setFont("Helvetica", 12)
c.drawString(50, 730, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
c.line(50, 720, 550, 720) # 画一条分割线

y_position = 680 # 初始 Y 坐标 (用来控制文字换行)

# 2. 核心分析逻辑：遍历每个产品
products = df['Product'].unique()

for prod in products:
    # 获取该产品的数据
    prod_data = df[df['Product'] == prod]
    
    # 获取今天和昨天的价格
    current_price = prod_data.iloc[-1]['Competitor_Price']
    cost = prod_data.iloc[-1]['My_Cost']
    
    # 计算利润空间
    margin = current_price - cost
    margin_percent = (margin / current_price) * 100
    
    print(f"正在分析: {prod}...")

    # --- 3. 自动画图 (matplotlib) ---
    plt.figure(figsize=(6, 3)) # 图稍微小一点，好放进 PDF
    plt.plot(prod_data['Date'], prod_data['Competitor_Price'], marker='o', color='red', linestyle='--')
    plt.title(f"7-Day Price Trend: {prod}")
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.grid(True)
    plt.tight_layout()
    
    # 临时保存图片
    chart_filename = f"temp_chart_{prod}.png"
    plt.savefig(chart_filename)
    plt.close() # 关掉图表，释放内存

    # --- 4. 写入 PDF ---
    # 如果页面快写满了，这就新建一页
    if y_position < 250:
        c.showPage()
        y_position = 750
    
    # 产品标题
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y_position, f"Product: {prod}")
    
    # 数据分析文字
    c.setFont("Helvetica", 10)
    c.drawString(50, y_position - 20, f"Current Competitor Price: ${current_price}")
    
    # 智能建议逻辑
    if margin_percent < 20:
        status = "DANGER: Low Margin! Do NOT drop price."
        c.setFillColorRGB(1, 0, 0) # 红色警告
    else:
        status = "OPPORTUNITY: Good Margin. You can lower price to compete."
        c.setFillColorRGB(0, 0.5, 0) # 绿色建议
        
    c.drawString(50, y_position - 40, f"Potential Margin: {margin_percent:.1f}%")
    c.drawString(50, y_position - 60, f"AI Advice: {status}")
    c.setFillColorRGB(0, 0, 0) # 恢复黑色

    # 插入刚才画的图表
    # drawImage(图片路径, x, y, 宽, 高)
    c.drawImage(ImageReader(chart_filename), 250, y_position - 110, width=300, height=150)
    
    # 清理临时图片 (假装它从来没存在过)
    os.remove(chart_filename)
    
    # 移动光标，准备写下一个产品
    y_position -= 160 
    c.line(50, y_position + 10, 550, y_position + 10) # 画一条细线分隔

# 5. 保存 PDF
c.save()
print("-" * 30)
print(f"🏆 任务完成！战略报告已生成: [{report_name}]")
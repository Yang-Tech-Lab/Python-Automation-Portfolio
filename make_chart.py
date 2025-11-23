import pandas as pd
import matplotlib.pyplot as plt

print("1. 正在读取数据...")
# 读取刚才算好的那个带结果的表格
df = pd.read_excel('fiverr_report_finished.xlsx')

print("2. 正在画图...")

# 设置画布大小 (宽10, 高6)
plt.figure(figsize=(10, 6))

# 画柱状图：X轴是产品，Y轴是销售总额，颜色是天蓝色
plt.bar(df['产品名称'], df['销售总额'], color='skyblue')

# 设置标题和标签 (用英文，防止中文乱码)
plt.title('Total Sales by Product (Fiverr Demo)', fontsize=16)
plt.xlabel('Product Name', fontsize=12)
plt.ylabel('Sales ($)', fontsize=12)

# 3. 保存图片
image_name = 'sales_chart.png'
plt.savefig(image_name)

print(f"✅ 成功！图表已保存为 [{image_name}]")
print("快去左边点开看看那张图片！")
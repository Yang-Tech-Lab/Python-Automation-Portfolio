import pandas as pd

print("1. 正在读取 Excel 文件...")
# 读取文件
df = pd.read_excel('fiverr_sales.xlsx')

# 2. 计算每一单赚了多少钱
df['销售总额'] = df['单价'] * df['销量']

# 3. 计算总收入 (用来给你自己看)
total_money = df['销售总额'].sum()
print(f"💰 今天的总收入是: ${total_money}")

print("4. 正在生成给客户的报表...")

# 5. 【最关键的一步】把算好的数据，保存成一个新的 Excel
# index=False 的意思是：不要把 0,1,2,3 这种行号写进去，客户不喜欢看
df.to_excel('fiverr_report_finished.xlsx', index=False)

print("✅ 搞定！[fiverr_report_finished.xlsx] 已保存到你的文件夹。")
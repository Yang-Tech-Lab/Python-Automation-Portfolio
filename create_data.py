import pandas as pd

print("正在制造假数据...")

# 1. 准备数据 (模拟 5 笔订单)
data = {
    '订单号': ['Order_001', 'Order_002', 'Order_003', 'Order_004', 'Order_005'],
    '产品名称': ['iPhone 15', 'MacBook Pro', 'AirPods', 'iPad Air', 'Apple Watch'],
    '单价': [999, 1999, 199, 599, 399],
    '销量': [2, 1, 5, 2, 3],
    '客户所在国': ['USA', 'UK', 'USA', 'China', 'Canada']
}

# 2. 把数据变成表格 (DataFrame)
df = pd.DataFrame(data)

# 3. 保存成 Excel 文件
file_name = 'fiverr_sales.xlsx'
df.to_excel(file_name, index=False)

print(f"成功！文件 [{file_name}] 已生成。")
print("快去左边的文件列表里看看，是不是多了一个 Excel 文件？")
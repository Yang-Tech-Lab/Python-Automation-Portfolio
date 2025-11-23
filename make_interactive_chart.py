import pandas as pd
import plotly.express as px

print("1. 正在读取数据...")
# 读取你之前生成的那个 Excel
df = pd.read_excel('fiverr_report_finished.xlsx')

print("2. 正在启动绘图引擎 (Plotly)...")

# 创建一个交互式柱状图
# x轴: 产品名称, y轴: 销售总额, color: 根据销售额变色
fig = px.bar(df, 
             x='产品名称', 
             y='销售总额',
             color='销售总额',
             title='Fiverr 销售数据交互式大屏 (把鼠标放上来试试！)',
             text_auto='.2s', # 自动显示数值
             template='plotly_dark') # 使用酷炫的深色模式

# 优化一下布局，让它看起来更像商业报表
fig.update_layout(
    xaxis_title="Product Name",
    yaxis_title="Total Sales ($)",
    font=dict(size=14)
)

# 3. 保存为网页文件 (.html)
output_file = "interactive_dashboard.html"
fig.write_html(output_file)

print(f"🎉 成功！交互式图表已保存为 [{output_file}]")
print("快去双击打开它，体验一下动态效果！")
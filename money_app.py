import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. 设置网页标题
st.title('💰 我的财富雪球预测机')
st.write('这是一个基于 Python 的交互式金融预测工具。')

# 2. 侧边栏：放控制钮
st.sidebar.header('⚙️ 参数设置')

# 拖动条：每月定投多少钱？
monthly_investment = st.sidebar.slider('每月定投金额 ($)', 100, 5000, 500)

# 拖动条：投多少年？
years = st.sidebar.slider('投资时长 (年)', 1, 30, 10)

# 拖动条：年化收益率 (默认设为 QQQ 的 15%)
annual_rate = st.sidebar.slider('预期年化收益率 (%)', 1, 30, 15)

# 3. 核心计算逻辑 (和之前一样)
months = years * 12
monthly_rate = (annual_rate / 100) / 12
future_value = 0
total_invested = 0
wealth_path = []

for i in range(months):
    future_value = future_value * (1 + monthly_rate) + monthly_investment
    total_invested += monthly_investment
    wealth_path.append(future_value)

profit = future_value - total_invested

# 4. 展示关键数据 (大字体)
col1, col2, col3 = st.columns(3)
col1.metric("总投入本金", f"${total_invested:,.0f}")
col2.metric("最终总资产", f"${future_value:,.0f}")
col3.metric("纯利润", f"${profit:,.0f}", delta_color="normal")

# 5. 画图 (直接在网页上画)
st.subheader('📈 财富增长曲线')
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(wealth_path, color='#FFD700', linewidth=3, label='Total Wealth')
ax.plot([0, months], [0, total_invested], color='gray', linestyle='--', label='Invested Cash')
ax.legend()
ax.grid(True, alpha=0.3)

# 把图表显示在网页上
st.pyplot(fig)

# 6. 底部版权
st.markdown("---")
st.caption("Developed by Yang | Powering your financial freedom")
from PyPDF2 import PdfWriter, PdfReader
from reportlab.pdfgen import canvas # 用来生成测试PDF的库
import os

print("🚀 PDF 合并工具启动...")

# --- 第一部分：先制造 2 个假 PDF 用来测试 ---
def create_dummy_pdf(filename, text):
    c = canvas.Canvas(filename)
    c.drawString(100, 750, text)
    c.save()
    print(f"📄 已生成测试文件: {filename}")

# 如果没有 reportlab 库，这步可能会报错，如果报错请在终端 pip install reportlab
try:
    create_dummy_pdf("contract_part1.pdf", "This is Page 1: Contract Header")
    create_dummy_pdf("contract_part2.pdf", "This is Page 2: Contract Details")
except:
    print("⚠️ 提示：请先运行 pip install reportlab 来生成测试文件")

# --- 第二部分：核心合并逻辑 (赚钱代码) ---
print("-" * 30)
print("🔗 开始合并 PDF...")

merger = PdfWriter()

# 要合并的文件列表
pdf_list = ["contract_part1.pdf", "contract_part2.pdf"]

for pdf in pdf_list:
    merger.append(pdf)
    print(f"➕ 已添加: {pdf}")

# 输出文件
output_filename = "merged_contract_final.pdf"
merger.write(output_filename)
merger.close()

print("-" * 30)
print(f"✅ 合并成功！新文件名为: [{output_filename}]")
print("快去打开看看，是不是两页变一页了？")
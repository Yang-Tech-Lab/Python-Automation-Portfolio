from PIL import Image, ImageDraw, ImageFont
import os

print("🚀 批量水印工厂启动...")

# --- 配置区 ---
input_folder = "Raw_Images"   # 原图文件夹
output_folder = "Watermarked_Images" # 处理后的文件夹
watermark_text = "Designed by Yang"  # 水印文字

# 创建输出文件夹
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# --- 核心处理逻辑 ---
file_list = os.listdir(input_folder)

for filename in file_list:
    # 只处理图片文件 (jpg, png)
    if filename.endswith(('.jpg', '.png', '.jpeg')):
        print(f"正在处理: {filename}...")
        
        # 1. 打开图片
        image_path = os.path.join(input_folder, filename)
        img = Image.open(image_path)
        width, height = img.size
        
        # 2. 准备画笔
        draw = ImageDraw.Draw(img)
        
        # 3. 设置字体 (这里用默认字体，稍微大一点)
        # 如果想用好看的字体，可以加载 .ttf 文件
        # 这里简单处理，根据图片宽度动态计算字体大小
        font_size = int(width / 10) 
        font = ImageFont.load_default() 
        
        # 4. 计算水印位置 (放在右下角)
        # textbbox 获取文字的宽和高 (left, top, right, bottom)
        bbox = draw.textbbox((0, 0), watermark_text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        x = width - text_width - 10
        y = height - text_height - 10
        
        # 5. 画上去！(红色水印)
        draw.text((x, y), watermark_text, font=font, fill=(255, 0, 0))
        
        # 6. 保存到新文件夹
        img.save(os.path.join(output_folder, filename))

print("-" * 30)
print(f"🎉 全部搞定！请去 [{output_folder}] 文件夹查看效果！")
from PIL import Image
print("Pillow 成功导入了！")
# 创建一个简单的 100x100 红色图片
img = Image.new('RGB', (100, 100), color = 'green')
img.save('test.png')
# 打印测试图片
print("测试图片 test.png 已生成！")
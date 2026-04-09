import numpy as np
from PIL import Image
import os
import time

def generate_noise_images(count=100, width=2000, height=2000, save_dir='images'):
    # 1. 如果文件夹不存在，则创建
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        print(f"文件夹 '{save_dir}' 已创建。")

    print(f"正在开始生成 {count} 张 {width}x{height} 的高清噪声图...")
    start_time = time.time()

    for i in range(1, count + 1):
        # 2. 生成随机像素数据 (RGB 三通道)
        # np.random.randint(低值, 高值, 形状, 数据类型)
        noise_array = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

        # 3. 将数组转换为图片对象
        img = Image.fromarray(noise_array)

        # 4. 保存图片
        file_path = os.path.join(save_dir, f'noise_{i:03d}.jpg')
        # 使用 quality=95 保证高清质量，如果你需要无损，可以改为 .png
        img.save(file_path, quality=95)

        if i % 10 == 0:
            print(f"进度: {i}/{count} 已完成")

    end_time = time.time()
    print(f"\n生成完毕！总耗时: {end_time - start_time:.2f} 秒。")
    print(f"图片保存在: {os.path.abspath(save_dir)}")

if __name__ == "__main__":
    generate_noise_images(100)
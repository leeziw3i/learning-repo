from PIL import Image
import os

def process_image(file_path):
    """
    打开图片，转为灰度(L模式)，并保存
    """
    # 1. 打开图片
    with Image.open(file_path) as img:
        # 2. 转换模式
        # 'L' 代表 Luminance (亮度)，是将 RGB 转换为 8 位像素的黑白效果
        grayscale_img = img.convert('L')
        
        # 3. 准备保存路径
        # 我们把处理后的图存到 images_gray/ 文件夹下，以免搞混
        parent_dir = os.path.dirname(file_path)
        base_name = os.path.basename(file_path)
        output_dir = os.path.join(os.path.dirname(parent_dir), 'images_gray')
        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        save_path = os.path.join(output_dir, f"gray_{base_name}")
        
        # 4. 保存
        grayscale_img.save(save_path)
        # print(f"已处理并保存: {save_path}")

# 批量处理逻辑
def batch_process(input_folder):
    files = [f for f in os.listdir(input_folder) if f.endswith('.jpg')]
    print(f"开始处理 {len(files)} 张图片...")
    
    for filename in files:
        full_path = os.path.join(input_folder, filename)
        process_image(full_path)
        
    print("所有图片处理完成！请查看 images_gray 文件夹。")

if __name__ == "__main__":
    batch_process('images')
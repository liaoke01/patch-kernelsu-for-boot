import os
import py7zr

# 获取当前工作目录
current_directory = os.getcwd()

# 设置7z文件的路径
archive_path = os.path.join(current_directory, 'magiskboot.7z')

# 设置解压路径（当前目录）
extract_path = current_directory

# 使用py7zr解压文件
with py7zr.SevenZipFile(archive_path, 'r') as z:
    z.extractall(extract_path)

print(f"文件已解压到: {extract_path}")

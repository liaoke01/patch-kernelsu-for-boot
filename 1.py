import py7zr

# 替换为你的7z文件路径
archive_path = 'magiskboot.7z'

# 替换为你想要解压到的目录路径
extract_path = './'

# 打开7z文件并解压
with py7zr.SevenZipFile(archive_path, 'r') as z:
    z.extractall(extract_path)

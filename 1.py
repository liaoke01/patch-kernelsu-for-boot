import py7zr

# 假设7z文件名为'archive.7z'，并且位于当前目录
archive_path = 'magiskboot.7z'

# 解压到当前目录
with py7zr.SevenZipFile(archive_path, 'r') as z:
    z.extractall()

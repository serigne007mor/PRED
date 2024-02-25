import os
import shutil

src_dir = './data/archives-EGC/'
dst_dir = './data/file_list/'

os.makedirs(dst_dir, exist_ok=True)
i = 0
for root, dirs, files in os.walk(src_dir):
    for file in files:
        src_file = os.path.join(root, file)
        dst_file = os.path.join(dst_dir, f'{i}_{file}')
        shutil.copy2(src_file, dst_file)
        i += 1
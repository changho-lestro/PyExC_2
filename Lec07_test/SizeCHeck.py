import os
from pathlib import Path
import pandas as pd

def get_folder_size(path):
    total = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            try:
                total += os.path.getsize(fp)
            except OSError:
                pass
    return total

# === CONFIGURE THIS PATH ===
root_dir = r"E:\Toolkit\Backup\EPPS93134\C"
# ===========================

root = Path(root_dir)
if not root.is_dir():
    raise ValueError(f"Invalid directory: {root_dir}")

folders = [f for f in root.rglob('*') if f.is_dir()]
data = []
for folder in folders:
    size = get_folder_size(folder)
    data.append({
        'Folder': folder.name,
        'Full Path': str(folder),
        'Size (Bytes)': size,
        'Size (MB)': size / (1024**2)
    })
df = pd.DataFrame(data)
df = df.sort_values('Size (Bytes)', ascending=False).reset_index(drop=True)

print(df.to_string(index=False))

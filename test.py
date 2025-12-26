import numpy as np

file_path = "./cub200_code_c2i_flip_ten_crop/cub200384_labels/1000.npy"
data = np.load(file_path)
print(data)

print("Shape:", data.shape)
print("dtype:", data.dtype)
print("content:", data)
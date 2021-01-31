import glob
import time
import pickle
import sys

def xingchens_images(dir_name):
    pattern_name = dir_name + '/**/*.[jbptJBPT][pnmiPNMI][gepfGEPF]'
    image_paths=[]
    image_paths.extend(glob.glob(pattern_name,recursive=True))
    pattern_name = dir_name + '/**/*.[jtJT][piPI][efEF][gfGF]'
    image_paths.extend(glob.glob(pattern_name,recursive=True))
    return image_paths

dir_path = sys.argv[1]
t1 = time.time()
data_path = 'data.pkl'
ret = xingchens_images(dir_path)
t2 = time.time()

with open(data_path, 'wb') as f:
    pickle.dump(ret, f)
with open(data_path,'rb') as f:
    ret_new = pickle.load(f)
print(ret==ret_new)
print(len(ret),' files using ', round(t2-t1,2),' sec')
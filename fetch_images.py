import glob
import time
import pickle
import sys
import datetime

def xingchens_images(dir_name):
    pattern_name = dir_name + '/**/*.[jbptJBPT][pnmiPNMI][gepfGEPF]'
    image_paths=[]
    image_paths.extend(glob.glob(pattern_name,recursive=True))
    pattern_name = dir_name + '/**/*.[jtJT][piPI][efEF][gfGF]'
    image_paths.extend(glob.glob(pattern_name,recursive=True))
    return image_paths

def dump_xingchens_images(image_paths, dump_path):
    with open(dump_path, 'wb') as f:
        pickle.dump(image_paths, f)

def restore_dumped_paths(dump_path):
    ret = []
    with open(dump_path,'rb') as f:
        ret = pickle.load(f)
    return ret

def whatTimeIsItNow():
    return datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

dir_path = sys.argv[1]
dump_path = whatTimeIsItNow()+'.pkl'

t1 = time.time()
image_paths = xingchens_images(dir_path)
t2 = time.time()

dump_xingchens_images(image_paths, dump_path)

print(image_paths==restore_dumped_paths(dump_path))
print(len(image_paths),' files using ', round(t2-t1,2),' sec')
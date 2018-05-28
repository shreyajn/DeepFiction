#ms5524
#sj2842
#as5446
import numpy as np
import pickle as pkl
#npz = np.load('/home/as5446/skip-thoughts/decoding/trial.npz')
#list_files = npz.files
#list_files = ['encoder_b.npy','encoder_U.npy']
mypath = '/home/as5446/skip-thoughts/decoding/dir_trial_npz'
from os import listdir
from os.path import isfile, join
list_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print list_files


new_array = []

for file in list_files:
    a = np.load('/home/as5446/skip-thoughts/decoding/dir_trial_npz/'+file)
    print a.shape
    print file
   
    if len(a.shape) == 2:
        for i in a:
            new_array.append(i)
    else:
        new_array.append(a)

n = np.array(new_array)

final = np.mean(n,axis=0)

np.save('childrens_book_style.npy',final)

#print final
#print final.shape


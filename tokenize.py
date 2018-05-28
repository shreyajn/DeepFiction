# import collections
# from collections import OrderedSet
# from orderedset import OrderedSet
#preprocessing children's book dataset
#ms5526
#as5446
import ast
import os
path_dir = '/home/maitri/Desktop/Columbia/SemesterII/DL4CV/project/CBTest/data'
rootdir = path_dir

import collections

class OrderedSet(collections.MutableSet):

    def __init__(self, iterable=None):
        self.end = end = [] 
        end += [None, end, end]         # sentinel node for doubly linked list
        self.map = {}                   # key --> [key, prev, next]
        if iterable is not None:
            self |= iterable

    def __len__(self):
        return len(self.map)

    def __contains__(self, key):
        return key in self.map

    def add(self, key):
        if key not in self.map:
            end = self.end
            curr = end[1]
            curr[2] = end[1] = self.map[key] = [key, curr, end]

    def discard(self, key):
        if key in self.map:        
            key, prev, next = self.map.pop(key)
            prev[2] = next
            next[1] = prev

    def __iter__(self):
        end = self.end
        curr = end[2]
        while curr is not end:
            yield curr[0]
            curr = curr[2]

    def __reversed__(self):
        end = self.end
        curr = end[1]
        while curr is not end:
            yield curr[0]
            curr = curr[1]

    def pop(self, last=True):
        if not self:
            raise KeyError('set is empty')
        key = self.end[1][0] if last else self.end[2][0]
        self.discard(key)
        return key

    def __repr__(self):
        if not self:
            return '%s()' % (self.__class__.__name__,)
        return '%s(%r)' % (self.__class__.__name__, list(self))

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return len(self) == len(other) and list(self) == list(other)
        return set(self) == set(other)



def get_tokenized_sentences(filepath):
	# final_list = []
	curr_set = OrderedSet()
	para = ""
	new_list = []
	with open(filepath,"r") as f:
			for line in f:
				if (line != " " and line != "" and line != "\n"):
					if new_list != [] and flag == 0:
						# output_file.write(str(new_list)+"\n")
						para += str(new_list) + "^|^"

				else:
					para = para[:-3]
					curr_set.add(para)
					para = ""


				flag = 0
				new_list = line.strip().split()
				new_list = new_list[1:]
				for i in range(len(new_list)):
					if new_list[i] == "-LRB-":
						new_list[i] = "("
					elif new_list[i] == "-RRB-":
						new_list[i] = ")"
					elif new_list[i] == "CHAPTER" or new_list[i] == "BOOK":
						flag = 1

	if new_list != [] and flag == 0:
		para += str(new_list)
	curr_set.add(para)

	output_file = open("/home/maitri/Desktop/Columbia/SemesterII/DL4CV/project/new_file.txt", "w")
	for item in curr_set:
		# print item 
		# break

		str_sentences = item.split("^|^")
		# print str_sentences
		# break
		
		for i in range(len(str_sentences)):
			if str_sentences[i] != "" and str_sentences[i] != " " and str_sentences[i] != "\n":
				x = ast.literal_eval(str_sentences[i])
				x = [n.strip() for n in x]
				x = " ".join(x)
		# 	# final_list.append(x)
				output_file.write(x+"\n")

	
	output_file.close()


if __name__ == '__main__':
	for subdir, dirs, files in os.walk(rootdir):
		for file in files:
			# print file
			get_tokenized_sentences(os.path.join(subdir, file))

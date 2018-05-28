#sj2842
#files made from the good caption and details file is used to make input_story.txt

import json
from collections import OrderedDict
r = open('/Users/shreyajain/Downloads/results.json').read()
data = json.loads(r)
#print data
f = open('/Users/shreyajain/Downloads/output.txt').read()
f2 = open('/Users/shreyajain/Downloads/input_story.txt','w')

text = f.split('\n')
for t in range(4,len(text)):
	l = text[t].split()
	
	if l!=[]:
		name = l[0].split('/')[-1]
		caption = l[1:]
		caption = ' '.join(caption)
		#print name,caption

		for i in data['results']:
			#print i['img_name']
			#print i['captions'][0:10]
			if name == i['img_name']:
				f2.write(name+'\t')
				f2.write(caption+'\t')
				#print(name+'\t'),
				#print(caption+'\t'),
				for k in i['captions'][0:10]:
					f2.write(k+'\t')
					#print(k+'\t'),i
					
				#print('\n')
				f2.write('\n')
				



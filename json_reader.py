#to read densecap results
#ms5524

import json
class unicode(unicode):
	def __repr__(self):
		return __builtins__.unicode.__repr__(self).lstrip("u")
#f1 = open('/Users/shreyajain/Desktop/output1234.txt','w')

data = json.load(open('/Users/shreyajain/Downloads/results (1).json'))
for i in range(len(data['results'])):
	print(data['results'][i]['img_name']+'\t')

	captions = []
	for j in data['results'][i]['captions']:
		j = unicode(j)
		print(j+',')
	print('\n')


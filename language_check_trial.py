#used to evaluate the grammar of the stories generated from three models
#average number of mistakes per story is given as output
#sj2842
#ms5526

import language_check
tool = language_check.LanguageTool('en-US')

with open("grammar.txt") as f:
	content = f.readlines()

content = [x.strip() for x in content]
content = [x.split("\t") for x in content]

for i in range(len(content)):
	for j in range(len(content[i])):
		content[i][j]  = content[i][j].replace('``','"')

model1 = []
model2 = []
model3 = []

for i in range(len(content)):
	for j in range(len(content[i])):
		# if i==2:
		text = content[i][j]
		# print(text)
		# print("***********************")
		matches = tool.check(text)
		if j==0:
			model1.append(len(matches))
		elif j==1:
			model2.append(len(matches))
		else:
			model3.append(len(matches))
	# print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

	# break


print(sum(model1) / float(len(model1)))
print(sum(model2) / float(len(model2)))
print(sum(model3) / float(len(model3)))

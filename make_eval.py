#as5446
#making files for langauge check
import glob
import generate
z = generate.load_all()
import generate2
y = generate2.load_all()
import generate3
w = generate3.load_all()
fil = open('/Users/shreyajain/Downloads/grammar.txt','w')
for filename in glob.iglob('/Users/shreyajain/Downloads/eval/*.jpg'):
    story = generate.story(z, filename,k=100, bw=50)
    story2 = generate2.story(y, filename,k=20, bw=5)
    story3 = generate3.story(w, filename,k=20, bw=5)
    print(story,story2,story3)
    fil.write(story+'\t'+story2+'\t'+story3)
    fil.write('\n')

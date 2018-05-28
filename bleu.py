#sj2842
#calculates the bleu score for evaluation
#done on test images for coco
#after captions are generated it can easily be run
import nltk
def sim(cap1,cap2):
    BLEUscore1 = nltk.translate.bleu_score.sentence_bleu(cap1, cap2, weights=(1,0,0,0))
   
    BLEUscore4 = nltk.translate.bleu_score.sentence_bleu(cap1, cap2, weights=(0,0,0,1))
    return BLEUscore1,BLEUscore4

    
   # print('\n')
    
f1 = open('predict.txt','r').read()
f2 = open('text.txt','r').read()
test2 = f2.split('\n')
num = len(test2)
test = f1.split('\n')
bleu1 = 0
bleu4 = 0
for t in test:
    l = t.split('\t')
    img = l[0]
    caption = l[1]
    for k in test2:
        m = k.split('\t')
        name = m[0]
        caps = m[1:]
        if m[0]==img:
            b1,b4=sim(caption,caps)
            bleu1+=b1
            bleu4+=b4
print bleu1/num,bleu/num




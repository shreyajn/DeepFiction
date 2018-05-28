#file was made to learn based on overlapp of bounding bozes which preposition should connect the two captions
#this was in an attempt to improve the image captions
#it did not work very well
#thus it is not being used
#sj2842


import pandas as pd
import math
import numpy
from sklearn.linear_model import LogisticRegression
eps=2.220446049250313e-16
import time
import gensim

def enclosingBoxArea(Box1,Box2):
    Box=[0 for x in range(4)]
    Box[0]=min(Box1[0]-(Box1[2]/2),Box1[0]+(Box1[2]/2),Box2[0]-(Box2[2]/2),Box2[0]+(Box2[2]/2))
    Box[1]=max(Box1[0]-(Box1[2]/2),Box1[0]+(Box1[2]/2),Box2[0]-(Box2[2]/2),Box2[0]+(Box2[2]/2))
    Box[2]=min(Box1[1]-(Box1[3]/2),Box1[1]+(Box1[3]/2),Box2[1]-(Box2[3]/2),Box2[1]+(Box2[3]/2))
    Box[3]=max(Box1[1]-(Box1[3]/2),Box1[1]+(Box1[3]/2),Box2[1]-(Box2[2]/2),Box2[1]+(Box2[3]/2))
    return((Box[1]-Box[0])*(Box[3]-Box[2]))

def IoU(Box1,Box2,S1,S2):
    lx1=Box1[0]-(Box1[2]/2)
    lx2=Box1[0]+(Box1[2]/2)
    ly1=Box1[1]-(Box1[3]/2)
    ly2=Box1[1]+(Box1[3]/2)
    tx1=Box2[0]-(Box2[2]/2)
    tx2=Box2[0]+(Box2[2]/2)
    ty1=Box2[1]-(Box2[3]/2)
    ty2=Box2[1]+(Box2[3]/2)
    SI= max(0, min(lx2, tx2) - max(lx1, tx1)) * max(0, min(ly2, tx2) - max(ly1, ty1))
    SU=S1+S2-SI
    return((SI+eps)/SU)

def Word2Vec(label):
    #print(label)
    if('-' in label):
        lab=label.split('-')
        label=lab[len(lab)-1]
    vec=model_EN[label]
    vec=list(vec)
    return vec

def OneHotFeature(label):
    feature=[0 for x in range(26)]
    for i in range(0,len(label)):
        if(ord(label[i])-97>0):
            feature[ord(label[i])-97]=1
    return feature


def extractfeatures(data):
    feat=[]
    features=[]
    y=data.loc[:][2]
    y=list(y)
    landmark=[]
    image=[]
    trajector=[]
    for i in range(0,len(data)):
        landmark_box=data.loc[i][9].split('-')
        trajector_box=data.loc[i][10].split('-')
        imageDim=data.loc[i][11].split('-')
        ld_box=[]
        tr_box=[]
        for j in range(0,len(landmark_box)):
             if landmark_box[j]=='':
                 continue
             else:
                ld_box.append(int(landmark_box[j]))
        for j in range(0,len(trajector_box)):
            if trajector_box[j]=='':
                continue
            else:
                tr_box.append(int(trajector_box[j]))

        landmark_box=ld_box
        trajector_box=tr_box
        x1=landmark_box[0]/(landmark_box[2]+eps)
        y1=landmark_box[1]/(landmark_box[3]+eps)
        x2=trajector_box[0]/(trajector_box[2]+eps)
        y2=trajector_box[1]/(trajector_box[3]+eps)
        feat.append(x2-x1)
        feat.append(y2-y1)
    
        AreaLandmark=landmark_box[2]*landmark_box[3]
        AreaTrajector=trajector_box[2]*trajector_box[3]
        feat.append(AreaLandmark/(AreaTrajector+eps))
        feat.append(landmark_box[2]/(landmark_box[3]+eps))
        feat.append(trajector_box[2]/(trajector_box[3]+eps))
    
        AreaEnclosing=enclosingBoxArea(landmark_box,trajector_box)
        feat.append((AreaLandmark)/(AreaEnclosing+eps))
        feat.append((AreaTrajector)/(AreaEnclosing+eps))
    
        feat.append(IoU(landmark_box,trajector_box,AreaLandmark,AreaTrajector))
    
        EuclDist=math.sqrt(math.pow(landmark_box[0]-trajector_box[0],2) + math.pow(landmark_box[1]-trajector_box[1],2))
        feat.append(EuclDist)
    
        Areaimg=int(imageDim[0])*int(imageDim[1])
        feat.append((AreaLandmark+eps)/Areaimg)
        feat.append((AreaTrajector+eps)/Areaimg)
#        print(type(feat)) 
        #check=['bowty','axe','a','graffitus','headscarve']
        #if(data.loc[i][4] in check or data.loc[i][3] in check):
            #continue
        feat=feat+Word2Vec(data.loc[i][4])
        feat=feat+Word2Vec(data.loc[i][3])
        #feat=feat+OneHotFeature(data.loc[i][4])
        #feat=feat+OneHotFeature(data.loc[i][3])
        print(len(feat))
        if len(feat)==611:
            features.append(feat)
            image.append(data.loc[i][0])
            landmark.append(data.loc[i][3])
            trajector.append(data.loc[i][4])
        else:
            hitlist.append(i)
        feat=[]
        #print(numpy.array(features).shape)
        if y[i] not in prep:
            prep.append(y[i])
        y[i]=prep.index(y[i])
    y=numpy.array(y)
    features=numpy.array(features)
    print(features.shape)
#    time.sleep(1)
    return features,y,image,trajector,landmark

        # print(features)
        # time.sleep(2)

model_EN = gensim.models.Word2Vec.load_word2vec_format("~/prepositions/GoogleNews-vectors-negative300.bin", binary=True)
#model_EN = gensim.models.Word2Vec.load_word2vec_format("~/prepositions/wiki2vec/torrents/enwiki-gensim-word2vec-1000-nostem-10cbow.torrent", binary=True)

data = pd.read_csv('~/prepositions/dataset/R201509/Flickr30k.highlevelcategory.train', sep='\t', header = None)
#data = pd.read_csv('~/prepositions/dataset/R201509/Flickr30k.majorityhead.train', sep='\t', header = None)
#data1 = pd.read_csv('~/prepositions/dataset/R201509/Flickr30k.highlevelcategory.test', sep='\t', header = None)
data1 = pd.read_csv('~/prepositions/answer3.txt', sep='\t', header = None)
#data1 = pd.read_csv('~/prepositions/dataset/R201509/Flickr30k.majorityhead.test', sep='\t', header = None)
print data1
prep1=list(data.loc[:][2].unique())
prep2=list(data1.loc[:][2].unique())
print prep2
#prep2=list(data1.loc[:][2].unique())
print len(prep1)
prep=prep1
prep.append('NA')
print prep
#prep=prep1+list(set(prep2)-set(prep1))
hitlist=[]
#training
features,y,image1,trajector1,landmark1=extractfeatures(data)

logit = LogisticRegression(multi_class='ovr')
logit.fit(features,y)

#testing
features1,y1,image,trajector,landmark=extractfeatures(data1)
print hitlist
#print(features.shape)
print(features1.shape)
predict=logit.predict(features1)
score=0
file1=open('output3.txt','w')
j=0
for i in range(0,len(predict)):
    print(prep[predict[i]])
    if j in hitlist:
        file1.write(' \n')
        j=j+1
    file1.write(image[i]+'\t')
    file1.write(trajector[i]+'\t')
    file1.write(landmark[i]+'\t')
    file1.write(prep[predict[i]])
    file1.write('\n')
    # print(prep[y1[i]])
    j=j+1
    if(predict[i]==y1[i]):
        score+=1
      #  print(score)
     #   time.sleep(1)
print(score)
print(len(predict))
print(score/(len(predict)*1.0))
print('done')

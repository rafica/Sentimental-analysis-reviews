import csv
import string
import nltk
x = nltk.porter.PorterStemmer()
maindict ={}
pos_doc_total = 0
neg_doc_total = 0

pos_word_total = 0
neg_word_total = 0
tfposdict = {}
tfnegdict = {}
flag = 0

stopwords = ['a', 'able', 'about', 'across', 'after', 'also', 'am', 'among', 'an', 'and', 'are', 'as', 'at', 'be', 'been', 'by', 'can', 'did', 'do', 'does', 'else', 'for', 'from', 'get', 'got', 'had', 'has', 'have', 'he', 'her', 'hers', 'him', 'his', 'how', 'i', 'if', 'in', 'into', 'is', 'it', 'its', 'let', 'like', 'likely', 'may', 'me', 'might', 'most', 'must', 'my', 'of', 'off', 'often', 'on', 'only', 'or', 'other', 'our', 'own', 'said', 'say', 'says', 'she', 'should', 'since', 'so', 'some', 'than', 'that', 'the', 'their', 'them', 'then', 'there', 'these', 'they', 'this', 'tis', 'to', 'twas', 'us', 'wants', 'was', 'we', 'were', 'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'will', 'with', 'would', 'yet', 'you', 'your']
import pickle       
            
filename = 'training_set.csv'


count = 0
with open(filename, 'rb') as f:
    reader = csv.reader(f)
 
    for row in reader:
        if flag==0:
            flag = 1
            continue
        localdict = {}

        if row[0] == '1':
            
        
            pos_doc_total = pos_doc_total + 1
            postext = row[1].translate(string.maketrans("",""), string.punctuation)
            postext = postext.lower()
            words_x = postext.split()
            #words= [w for w in words_x if not w in stopwords]
            for word in words_x:
                word = x.stem(word)
                pos_word_total = pos_word_total + 1
                if word in tfposdict:
                    tfposdict[word] = tfposdict[word] + 1
                else:
                    tfposdict[word] = 1
                
                if word in localdict:
                    localdict[word] = localdict[word]+1
                else:
                    localdict[word] = 1
                
            for key in localdict:
                if key in maindict:
                    if 'N11' in maindict[key]:
                        maindict[key]['N11'] = maindict[key]['N11'] + 1
                    else:
                        maindict[key]['N11'] = 1
                        
                else:
                    maindict[key] = {}
                    maindict[key]['N11'] = 1
                
        else:
            neg_doc_total = neg_doc_total + 1
            negtext = row[1].translate(string.maketrans("",""), string.punctuation)
            negtext = negtext.lower()
            words_x = negtext.split()
            #words = [w for w in words_x if not w in stopwords]
            
            for word in words_x:
                word = x.stem(word)
                neg_word_total = neg_word_total + 1
                if word in tfnegdict:
                    tfnegdict[word] = tfnegdict[word] + 1
                else:
                    tfnegdict[word] = 1
                if word in localdict:
                    localdict[word] = localdict[word]+1
                else:
                    localdict[word] = 1
            for key in localdict:
                if key in maindict:
                    if 'N10' in maindict[key]:
                        maindict[key]['N10'] = maindict[key]['N10'] + 1
                    else:
                        maindict[key]['N10'] = 1
                        #print maindict[key]['N10']
                else:
                    maindict[key] = {}
                    maindict[key]['N10'] = 1
   
for key in maindict:
    if 'N11' not in maindict[key]:
        maindict[key]['N11'] = 0
    maindict[key]['N01'] = pos_doc_total - maindict[key]['N11']
    if 'N10' not in maindict[key]:
        maindict[key]['N10'] = 0
    maindict[key]['N00'] = neg_doc_total - maindict[key]['N10']
   






################################## trigrams ###############################################

tfposdict_trigram = {}
tfnegdict_trigram = {}
count = 0
maindict_trigram = {}
pos_word_trigram_total = 0
neg_word_trigram_total = 0
flag= 0
with open(filename, 'rb') as f:
    reader = csv.reader(f)
 
    for row in reader:
        if flag == 0:
            flag = 1
            continue
        localdict_trigram = {}
        
        if row[0] == '1':
            postext = row[1].translate(string.maketrans("",""), string.punctuation)
            postext = postext.lower()
            words = postext.split()
       
            
            for i in range(0,len(words)-3):
                trigram = (words[i],words[i+1],words[i+2])
                imp_stop = ("well", "not", "but", "comedy","funny",)
                if set(trigram).intersection(set(imp_stop)):
                    pos_word_trigram_total = pos_word_trigram_total + 1
                    if trigram in tfposdict_trigram:
                        tfposdict_trigram[trigram] = tfposdict_trigram[trigram] + 1
                    else:
                        tfposdict_trigram[trigram] = 1
                    
                    
                    if trigram in localdict_trigram:
                        localdict_trigram[trigram] = localdict_trigram[trigram] + 1
                    else:
                        localdict_trigram[trigram] = 1
                
            for key in localdict_trigram:
                    
                if key in maindict_trigram:
                    if 'N11' in maindict_trigram[key]:
                        maindict_trigram[key]['N11'] = maindict_trigram[key]['N11'] + 1
                    else:
                        maindict_trigram[key]['N11'] = 1
                        
                else:
                    maindict_trigram[key] = {}
                    maindict_trigram[key]['N11'] = 1
                
        else:
            negtext = row[1].translate(string.maketrans("",""), string.punctuation)
            negtext = negtext.lower()
            words = negtext.split()

            for i in range(0,len(words)-3):
                trigram = (words[i],words[i+1],words[i+2])
                imp_stop = ("not","but","neither","nor","overly","just","only")
                if set(trigram).intersection(set(imp_stop)):
                    neg_word_trigram_total = neg_word_trigram_total + 1
                    if trigram in tfnegdict_trigram:
                        tfnegdict_trigram[trigram] = tfnegdict_trigram[trigram] + 1
                    else:
                        tfnegdict_trigram[trigram] = 1
                    if trigram in localdict_trigram:
                        localdict_trigram[trigram] = localdict_trigram[trigram]+1
                    else:
                        localdict_trigram[trigram] = 1
            for key in localdict_trigram:
                if key in maindict_trigram:
                    if 'N10' in maindict_trigram[key]:
                        maindict_trigram[key]['N10'] = maindict_trigram[key]['N10'] + 1
                    else:
                        maindict_trigram[key]['N10'] = 1
                        #print maindict[key]['N10']
                else:
                    maindict_trigram[key] = {}
                    maindict_trigram[key]['N10'] = 1
   
for key in maindict_trigram:
    if 'N11' not in maindict_trigram[key]:
        maindict_trigram[key]['N11'] = 0
    maindict_trigram[key]['N01'] = pos_doc_total - maindict_trigram[key]['N11']
    if 'N10' not in maindict_trigram[key]:
        maindict_trigram[key]['N10'] = 0
    maindict_trigram[key]['N00'] = neg_doc_total - maindict_trigram[key]['N10']
   



#-----------------calculating chi value-----------------#

X ={}

for key in maindict:
    numerator = (maindict[key]['N11'] + maindict[key]['N10'] + maindict[key]['N01'] + maindict[key]['N00'])*(maindict[key]['N11']*maindict[key]['N00']-maindict[key]['N10']*maindict[key]['N01'])**2
    denom = (maindict[key]['N11'] + maindict[key]['N01'])*(maindict[key]['N11'] + maindict[key]['N10']) * (maindict[key]['N10'] + maindict[key]['N00']) * (maindict[key]['N01'] + maindict[key]['N00'])

    X[key] = numerator/denom

output = sorted(X.items(), key=lambda x:x[1], reverse = True)

count = 0

feature = len(output)

vocab = []
for i in output:
    count = count + 1
    if count == feature:
        break
    vocab.append(i[0])

    
################################################


X_trigram ={}



for key in maindict_trigram:
    numerator = (maindict_trigram[key]['N11'] + maindict_trigram[key]['N10'] + maindict_trigram[key]['N01'] + maindict_trigram[key]['N00'])*(maindict_trigram[key]['N11']*maindict_trigram[key]['N00']-maindict_trigram[key]['N10']*maindict_trigram[key]['N01'])**2
    denom = (maindict_trigram[key]['N11'] + maindict_trigram[key]['N01'])*(maindict_trigram[key]['N11'] + maindict_trigram[key]['N10']) * (maindict_trigram[key]['N10'] + maindict_trigram[key]['N00']) * (maindict_trigram[key]['N01'] + maindict_trigram[key]['N00'])
    
    X_trigram[key] = numerator/denom

output_trigram = sorted(X_trigram.items(), key=lambda x:x[1], reverse = True)
vocab_trigram = []
count = 0

feature_trigram = len(output_trigram)
for i in output_trigram:
    count = count+1
    
    if count == feature_trigram:
        break
    vocab_trigram.append(i[0])





#Naive bays
count = 0
correct = 0
total = 0
docid = 1
P = {}
P['pos'] ={}
P['neg'] ={}
posoccur = 0
negoccur = 0

P_trigram = {}
P_trigram['pos'] = {}
P_trigram['neg'] = {}
posoccur_trigram = 0
negoccur_trigram = 0
Ppos_num = {}
Pneg_num = {}
#with open('test.csv', 'rb') as f:
    #reader = csv.reader(f)
#print tfposdict


        
       
        
P_pos_final = pos_doc_total*1.0/((pos_doc_total + neg_doc_total)*1.0)
P_neg_final = neg_doc_total*1.0/((pos_doc_total + neg_doc_total)*1.0)
compare = row[0]

prior = [P_pos_final,P_neg_final]


        

for word in vocab:
    if word in tfposdict:
        posoccur = tfposdict[word]
    else:
        posoccur = 0
    if word in tfnegdict:
        negoccur = tfnegdict[word]
    else:
        negoccur = 0


    P['pos'][word] = (posoccur + 1)*1.0/((pos_word_total + feature+ pos_word_trigram_total + feature_trigram)*1.0)
    P['neg'][word] = (negoccur + 1)*1.0/((neg_word_total + feature+ neg_word_trigram_total + feature_trigram)*1.0)

              
        

for trigram in vocab_trigram:
    if trigram in tfposdict_trigram:
        posoccur_trigram = tfposdict_trigram[trigram]
    else:
        posoccur_trigram = 0
    if trigram in tfnegdict_trigram:
        negoccur_trigram = tfnegdict_trigram[trigram]
    else:
        negoccur_trigram = 0

    P_trigram['pos'][trigram] = (posoccur_trigram + 1)*1.0/((pos_word_total + feature + pos_word_trigram_total + feature_trigram)*1.0)
    P_trigram['neg'][trigram] = (negoccur_trigram + 1)*1.0/((neg_word_total + feature + neg_word_trigram_total + feature_trigram)*1.0)



modelfile = {}
modelfile["P"] = P
modelfile["P_trigram"] = P_trigram
modelfile["prior"] = prior
pickle.dump(modelfile, open('model_file.p', 'wb'))
     


            
               
            
            
            



            

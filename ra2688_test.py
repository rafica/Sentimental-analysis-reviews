import pickle
import csv
import string
import nltk
stopwords = ['a', 'able', 'about', 'across', 'after', 'also', 'am', 'among', 'an', 'and', 'are', 'as', 'at', 'be', 'been', 'by', 'can', 'did', 'do', 'does', 'for', 'from', 'get', 'got', 'had', 'has', 'have', 'he', 'her', 'hers', 'him', 'his', 'how', 'i', 'if', 'in', 'into', 'is', 'it', 'its', 'let', 'like', 'likely', 'may', 'me', 'might', 'most', 'must', 'my', 'of', 'off', 'often', 'on', 'only', 'or', 'other', 'our', 'own', 'said', 'say', 'says', 'she', 'should', 'since', 'so', 'some', 'than', 'that', 'the', 'their', 'them', 'then', 'there', 'these', 'they', 'this', 'tis', 'to', 'twas', 'us', 'wants', 'was', 'we', 'were', 'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'will', 'with', 'would', 'yet', 'you', 'your']
x = nltk.porter.PorterStemmer()

count = 0

total = 0
docid = 1
Ppos = {}
Pneg = {}

posoccur = 0
negoccur = 0

posoccur_trigram = 0
negoccur_trigram = 0
Ppos_num = {}
Pneg_num = {}
#with open('test.csv', 'rb') as f:
    #reader = csv.reader(f)
#print tfposdict
modelfile = {}
P={}
P_trigram ={}
prior ={}
modelfile = pickle.load(open('model_file.p', 'rb'))
P = modelfile["P"]
P_trigram= modelfile["P_trigram"]
prior = modelfile["prior"]

flag = 0
output = {}

with open('test_set.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if flag==0:
           flag=1
           continue
        total = total + 1
        P_pos_final = prior[0]
        P_neg_final = prior[1]
        
        #print P_pos_final
        
        testtxt = row[0].translate(string.maketrans("",""), string.punctuation)
        testtxt = testtxt.lower()
        words = testtxt.split()
        words_stop= [w for w in words if not w in stopwords]
        words_stem=[]
        words_stop_stem=[]
        for word in words:
            word = x.stem(word)
            words_stem.append(word)
        for word in words_stop:
            word = x.stem(word)
            words_stop_stem.append(word)
        for word in words_stem:
            if word in P['pos']:
            
                P_pos_final = P_pos_final*1.0 * P['pos'][word]*1.0
            if word in P['neg']:
                P_neg_final = P_neg_final*1.0 * P['neg'][word]*1.0
        
        for i in range(0,len(words)-3):
            trigram = (words[i],words[i+1],words[i+2])
            if trigram in P_trigram['pos']:
                P_pos_final = P_pos_final*1.0 * P_trigram['pos'][trigram]*1.0
            if trigram in P_trigram['neg']:
                P_neg_final = P_neg_final*1.0 * P_trigram['neg'][trigram]*1.0
            
        
        #print Ppos[word]
        #print Pneg[word]
        """    
            test_num = len(words)
            if test_num not in Ppos_num:
                if test_num in vocab_num:
                    if test_num in pos_num_words:
                        posoccur_num = pos_num_words[test_num]
                    else:
                        posoccur_num = 0
                    if test_num in neg_num_words:
                        negoccur_num = neg_num_words[test_num]
                    else:
                        negoccur_num = 0
                else:
                    posoccur_num = 0
                    negoccur_num = 0
                Ppos_num[test_num] = (posoccur_num + 1)*1.0/((pos_word_total + feature + pos_word_trigram_total + feature_trigram)*1.0)
                Pneg_num[test_num] = (negoccur_num + 1)*1.0/((neg_word_total + feature + neg_word_trigram_total + feature_trigram)*1.0)
            
            P_pos_final = P_pos_final*1.0 * Ppos_num[test_num]*1.0
            P_neg_final = P_neg_final*1.0 * Pneg_num[test_num]*1.0

        """
   
        if P_pos_final > P_neg_final:
            output[docid] = "1"        
        else:
            output[docid] = "0"
        docid = docid + 1

f = open('prediction_file.csv', 'wb')
writer = csv.writer(f)
writer.writerow(["Id","Category"])
for key, value in output.items():
   writer.writerow([key, value])
f.close()


       

   
         
   

            
               
            
            
            



            

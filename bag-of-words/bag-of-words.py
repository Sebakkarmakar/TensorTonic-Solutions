import numpy as np

def bag_of_words_vector(tokens, vocab):
   
    vector=[]
    if len(vocab)==0:
        return np.array(vector,dtype=int)
    for i in vocab:
        if i in tokens:
            vector.append(tokens.count(i))
        else:
             vector.append(int(0))
    return np.array(vector,dtype=int)
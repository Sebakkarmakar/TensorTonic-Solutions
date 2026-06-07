def word_count_dict(sentences):
    hashmap={}
    words=[]
    for i in sentences:
        for word in i:
            
            if word in hashmap:
                hashmap[word]+=1
            else:
                hashmap[word]=1
    return hashmap
def remove_stopwords(tokens, stopwords):
    filted_array=[]
    for i in tokens:
        if i not in stopwords:
            filted_array.append(i)
    return filted_array
    
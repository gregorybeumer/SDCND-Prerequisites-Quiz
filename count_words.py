def count_words(s, n):
    words_list = s.split()
    words_dict = {}
    for word in words_list:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1
            
    words_list = []
    for key, value in words_dict.iteritems():
        words_list.append((key,value))
    
    words_list.sort(key=lambda item: (-item[1], item[0]))
    
    return words_list[:n]
    
print count_words("betty bought a bit of butter but the butter was bitter", 3)

def check_pangram(s):
    ch_list=[]
    for i in range(26): 
        ch_list.append(False)
    print(ch_list)
    for c in s.lower():
        if not c==" ":
            print(ord(c)-ord('a'))
            ch_list[ord(c)-ord('a')] = True
    for ch in ch_list:
        if ch == False:
            return False
    return True

sentence = "The qick brown fox jmps over the little lazy dg"
print(check_pangram(sentence))
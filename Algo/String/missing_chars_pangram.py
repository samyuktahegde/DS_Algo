def missing_characters_pangram(s):
    ch_list = [False]*26
    for c in s.lower():
        if not c==" ":
            ch_list[ord(c)-ord('a')] = True
    print(ch_list)
    for ch in ch_list:
        if ch == False:
            print(chr(ch))

sentence = "The quick brown fox jumps over the little lazy dug"
missing_characters_pangram(sentence)
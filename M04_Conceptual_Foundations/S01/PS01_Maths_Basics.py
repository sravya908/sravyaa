def Frequency_count(s):
    d = {}
    for ch in s:
        if ch not in d:
            d[ch] = 1
        else: 
            d[ch] += 1
    return d
print(Frequency_count("abcabc"))

def Anagrams(str1,str2):
    pass
print(Anagrams("paces","space"))
print(Anagrams("aabbcc","abc")) 
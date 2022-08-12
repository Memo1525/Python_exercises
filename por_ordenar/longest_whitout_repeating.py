def lengthOfLongestSubstring(self, s):
    s="abcabcbb"
    dic, res, start, = {}, 0, 0
    for i, ch in enumerate(s): #cuenta los elementos y los itera 
        if ch in dic:
            res = max(res, i-start) # update the res #aqui esto nos da 2
            start = max(start, dic[ch]+1)  # here should be careful, like "abba"
        dic[ch] = i #{a:o}{b:0}{c:0} 
    return max(res, len(s)-start)  # return should consider the last non-repeated substring


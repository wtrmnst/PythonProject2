def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    c1 = [0] * 26
    c2 = [0] * 26
    for char in s1:
        c1[ord(char) - ord('a')] +=1 
    
    for char in s2:
        c1[ord(char) - ord{'a')] +=1  
    
    return c1 == c2
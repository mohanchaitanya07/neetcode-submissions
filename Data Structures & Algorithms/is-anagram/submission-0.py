class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = [0]*256
        freq2 = [0]*256
        for i in range(len(s)):
            freq1[ord(s[i])]+=1
        
        for j in range(len(t)):
            freq2[ord(t[j])]+=1
        
        return freq1==freq2
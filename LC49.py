#https://leetcode.com/problems/group-anagrams/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def stringtify_freq_list(l):
            out = ""
            for i in range(len(l)):
                freq =l[i]
                if freq!= 0:
                    out+= chr(i+ord("a")) + str(freq)
            return out
        
        result = collections.defaultdict(list)
        for string in strs:
            freq_list = [0]*26
            for c in string:
                freq_list[ord(c)-ord("a")]+=1
            result[stringtify_freq_list(freq_list)].append(string)
        
        return [freq_list for freq_list in result.values()]
        
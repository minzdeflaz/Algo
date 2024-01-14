#https://leetcode.com/problems/sentence-screen-fitting/
from typing import List
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        lenWords = []
        maxLen = 0
        for word in sentence:
            lenWord = len(word) + 1
            maxLen = max(maxLen, lenWord)
            lenWords.append(lenWord)
        cols+=1
        if maxLen > cols:
            return 0
        
        i = 0
        leftOver = cols
        rowCount = 0
        senCount = 0
        while True:
            if i == len(lenWords):
                senCount+=1
                if leftOver <= 0 or leftOver - lenWords[0]:
                    rowCount+=1
                    break
                i = 0
            curLen = lenWords[i]

            if curLen > leftOver:
                leftOver = cols - curLen
                rowCount+=1
                if rowCount >= rows:
                    return senCount
            elif curLen <= leftOver:
                leftOver -= curLen
            i+=1
        return int(rows / rowCount * senCount)

            
if __name__  == "__main__":
    sentence = ["a"]
    rows = 2
    cols = 2
    sol = Solution()
    print(sol.wordsTyping(sentence, rows, cols))
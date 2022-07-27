#https://leetcode.com/problems/sentence-screen-fitting/



class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        if max(len(word) for word in sentence) > cols:
            return 0
        
        rowNeed = 0
        curRow = 0
        senCnt = 0
        while True:
            if rowNeed > rows:
                break
            for word in sentence:
                curRow += len(word)
                if curRow <= cols:
                    curRow += 1
                else:
                    rowNeed += 1
                    curRow = 0
            sentence += 1
        
#https://leetcode.com/problems/sentence-screen-fitting/



class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        lenSen = [len(word) for word in sentence]
        if max(lenSen) > cols:
            return 0
        rowNeed = 1
        curRow = 0
        senCnt = 0
        while True:
            for lenWord in lenSen:
                curRow += lenWord
                if curRow <= cols:
                    curRow += 1
                else:
                    rowNeed += 1
                    curRow = lenWord + 1
            if rowNeed >= rows + 1:
                break
            senCnt += 1
        return senCnt
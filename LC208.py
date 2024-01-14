#https://leetcode.com/problems/implement-trie-prefix-tree/
class Trie:

    def __init__(self, char="", full=False):
        self.val = char
        self.full = full
        self.children = [None]*26

    def insert(self, word: str,i =0) -> None:
        if i == len(word):
            self.full = True
            return
        char = word[i]
        int_char = ord(word[i]) - ord("a")
        if not self.children[int_char]:
            self.children[int_char] = Trie(char)
        self.children[int_char].insert(word, i+1)


    def search(self, word: str, i = 0, search = True) -> bool:
        if i == len(word):
            return self.full if search else True
        char = word[i]
        int_char = ord(word[i]) - ord("a")
        if self.children[int_char] and self.children[int_char].val == char:
            return self.children[int_char].search(word, i+1, search)
        return False

    def startsWith(self, prefix: str, i = 0) -> bool:
        return self.search(prefix, i, False)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
#https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
      q = []
      for tok in tokens:
        if tok.isnumeric() or str(tok[1::]).isnumeric():
          q.append(int(tok))
        else:
          num2 = q.pop()
          num1 = q.pop()
            
          if tok == "+":
            q.append(num1 + num2)
          elif tok == "/":
            q.append(int(num1 / num2))
          elif tok == "*":
            q.append(num1 * num2)
          elif tok == "-":
            q.append(num1 - num2)
          elif tok.startswith("-"):
            q.append(int(tok))
      return q.pop()

if __name__ == "__main__":
  a = Solution()
  test = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
  print(a.evalRPN(test))

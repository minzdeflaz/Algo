#https://leetcode.com/problems/house-robber/
def solution(nums: list[int]) -> int:
    best = [0,0]
    best.extend(nums)
    best.extend([0,0])
    for i in range(3,len(best)):
        best[i] += max(best[i-2], best[i-3])
    return max(best[-1], best[-2])
if __name__ == "__main__":
    tests = [
        ([1,2,3,1], 4),
        ([2,7,9,3,1] , 12),
        ([4,2,3,4,3,3,1], 11)
    ]
    for test, result in tests:
        if solution(test) == result:
            print(f"test passed:{test}: {result}")
        else:
            print(f"test failed:{test}: {result}")
    

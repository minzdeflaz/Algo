#https://leetcode.com/problems/house-robber-ii/
def get_last_bests(nums: list[int]) -> int:
    best = [0,0]
    best.extend(nums)
    best.extend([0,0])
    for i in range(3,len(best)):
        best[i] += max(best[i-2], best[i-3])
    return (best[-1], best[-2])

def solution(nums: list[int]) -> int:
    if len(nums)==3:
        return max(nums)
    
    best1, best2 = get_last_bests(nums)
    new_best1, new_best2 = get_last_bests(nums[1::] + nums[0:1:])
    if len(nums) %2:
        return min(min(best1, new_best2), min(best2, new_best1))
    else:
        if best1 > best2:
            return best1 if best1 == new_best2 else max(new_best2, best2)
        return best2
    
if __name__ == "__main__":
    tests = [
        ([2,3,2], 3),
        ([2,3,2,2], 5),
        ([1,2,3,4] , 6),
        ([1,2,3,4,1] , 6),
        ([1,2,3], 3),
        ([3,2,1], 3),
        ([3,2,1,3], 5),
        ([3,2,3,4,5,6,7,8], 20)
    ]
    for test, result in tests:
        if (sol:=solution(test)) == result:
            print(f"test passed:{test}=> {result}")
        else:
            print(f"test failed:{test}=> {sol} instead of {result}")
    
    
#1,5,8 =>9,5
#5,8,1=> 6,8
#8,1,5 => 13,1
            
#1,4,6,7 =>11,7
#4,6,7,1 => 7, 11

#3,1,6,8 => 11,9
#1,6,8,3 => 9,9

#1,4,5,3,9 => 15,7
#4,5,3,9,1 => 8, 14

#3,2,1,3 => 6,4
#2,1,3,3 => 4,5
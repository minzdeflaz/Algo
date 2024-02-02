#https://leetcode.com/problems/dot-product-of-two-sparse-vectors/
class SparseVector:
    def __init__(self, nums: List[int]):
        self.num_map = {loc:val for loc,val in enumerate(nums) if val !=0}
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for loc in self.num_map:
            if loc in vec.num_map:
                res += vec.num_map[loc]* self.num_map[loc]
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
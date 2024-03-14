//https://leetcode.com/problems/kth-largest-element-in-a-stream/submissions/1196155608/
public class KthLargest {
    PriorityQueue<int, int> minHeap;
    public int k;
    public KthLargest(int k, int[] nums) {
        this.k = k;
        minHeap = new();
        foreach(var num in nums){
            Add(num);
        }
    }
    
    public int Add(int val) {
        minHeap.Enqueue(val,val);
        if (minHeap.Count > k){
            minHeap.Dequeue();
        }
        return minHeap.Peek();
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.Add(val);
 */
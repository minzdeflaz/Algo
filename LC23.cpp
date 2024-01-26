//https://leetcode.com/problems/merge-k-sorted-lists/submissions/1097634392/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
 //1,1,2
 //out:1
 //4,1,2
 //out:1,1
 // O(nlogn)
 // 1,1,2
 // 4,1,2
 // min-heap: O(k) -> O(n) on average

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<int, vector<int>, greater<int>> pq;
        for(auto &item: lists){
            if (item != NULL){
                pq.push(item->val);
            }
        }
        ListNode* curr_node = new ListNode();
        ListNode* res = curr_node;
        while(!pq.empty()){
            int curr = pq.top();
            pq.pop();
            curr_node->val = curr;
            
            for (int i=0; i<lists.size(); i++){
                if(lists[i] && lists[i]->val == curr){
                    lists[i] = lists[i]->next;
                    if (lists[i]!=nullptr){
                        pq.push(lists[i]->val);
                    }
                    break;
                }
                
            }
            if (!pq.empty()){
                ListNode *nextt = new ListNode();
                curr_node->next = nextt;
                curr_node = nextt;
            }
        }
        if (res->val == 0 && res->next == nullptr){
            return nullptr;
        }
        return res;
    }
};
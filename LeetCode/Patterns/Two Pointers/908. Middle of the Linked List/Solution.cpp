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
class Solution {
public:
    int len(ListNode* head){

        ListNode* temp = head;
        int l = 0;

        while(temp){
            l++;
            temp = temp->next;

        }
        return l;
    }

    ListNode* middleNode(ListNode* head){
        ListNode* temp = head;
        int l = len(head);

        int cnt = 0;
        while(cnt!=(l/2)){
            temp = temp->next;
            cnt++;

        }
        return temp;

    }
        
    
};
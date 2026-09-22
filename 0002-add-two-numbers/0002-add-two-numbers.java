/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
// class Solution {
//     public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
//         StringBuilder s1 = new StringBuilder();
//         for(int i=l1.length-1;i<=0;i--){
//             s1.append(l1[i]);
//         }
//         StringBuilder s2 = new StringBuilder();
//         for(int i=l2.length-1;i<=0;i--){
//             s2.append(l2[i]);
//         }
//         String str1 = s1.toString();
//         String str2 = s2.toString();
//         int num1 = Integer.parseInteger(str1);
//         int num2 = Integer.parseInteger(str2);
//         int sum = num1+num2;
//         String s = sum.toString();
//         List<Integer> fl = new ArrayList<>();
//         for(char ch : sum.toCharArray()){
//             fl.add(Character.getNumericValue(ch));
//         }
        
//         return fl;
//     }
// }

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode result = new ListNode(0);
        ListNode ptr = result;
        int carry =0;
        while(l1!=null || l2!=null){
            int sum = carry;
            if(l1!=null){
                sum+=l1.val;
                l1=l1.next;
            }
            if(l2!=null){
                sum+=l2.val;
                l2=l2.next;
            }
            carry =sum/10;
            sum=sum%10;
            ptr.next=new ListNode(sum);
            ptr = ptr.next;
        }
        if(carry ==1)
            ptr.next = new ListNode(1);
        return result.next;
    }
}
        
        
        
        
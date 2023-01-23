/* Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0 */

class Solution {
    public int firstUniqChar(String s) {
        HashMap<Character,Integer>map=new HashMap<>();
        for(int i=0;i<s.length();i++){
            char ch =s.charAt(i);
            if(map.containsKey(ch))
            {
                map.put(ch,map.get(ch)+1);

            }
            else
            {
                map.put(ch,1);

            }

        }
        for(int i=0;i<s.length();i++)
        {
             int freq=map.get(s.charAt(i));
             if(freq==1){
                 return i;
             }
        }
        return -1;

        
    }
}

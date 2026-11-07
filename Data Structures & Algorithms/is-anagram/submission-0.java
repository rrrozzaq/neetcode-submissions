class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }

        HashMap<Character, Integer> boxS = new HashMap<>();
        HashMap<Character, Integer> boxT = new HashMap<>();

        for(int i = 0; i < s.length(); i++){
            boxS.put(s.charAt(i), boxS.getOrDefault(s.charAt(i), 0) + 1);
            boxT.put(t.charAt(i), boxT.getOrDefault(t.charAt(i), 0) + 1);
        }
        return boxS.equals(boxT);
    }
}

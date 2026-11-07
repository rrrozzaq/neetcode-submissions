class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> box = new HashMap<>();

        for (String s : strs){
            int[] count = new int[26];
            for (char c : s.toCharArray()){
                count[c-'a']++;
            }
            String key = Arrays.toString(count);
            box.putIfAbsent(key, new ArrayList<>());
            box.get(key).add(s);
        }
        return new ArrayList<>(box.values());
    }
}

class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> box = new HashSet<Integer>();

        for(int i = 0; i < nums.length; i++){
            if(box.contains(nums[i])){
                return true;
            }
            box.add(nums[i]);
        }
        
        return false;
    }
}
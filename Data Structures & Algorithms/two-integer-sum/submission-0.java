class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> box = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            int diff = target - nums[i];
            if(box.containsKey(diff)){
                return new int[] {box.get(diff), i};
            }
            box.put(nums[i], i);
        }
        return new int[0];
    }
}

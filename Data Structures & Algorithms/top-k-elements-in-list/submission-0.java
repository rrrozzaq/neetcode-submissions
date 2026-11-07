class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> box = new HashMap<>();
        List<Integer>[] freq = new List[nums.length + 1];

        // buat arraylist kosong untuk freq
        for(int i = 0;i < freq.length; i++){
            freq[i] = new ArrayList<>();
        }

        for(int n : nums){
            box.put(n, box.getOrDefault(n, 0) + 1);
        }

        for(Map.Entry<Integer, Integer> entry : box.entrySet()){
            freq[entry.getValue()].add(entry.getKey());
        }

        int[] res = new int[k];
        int index = 0;
        for(int i = freq.length - 1; i > 0 && index < k; i--){
            for (int n : freq[i]) {
                res[index++] = n;
                if (index == k) {
                    return res;
                }
            }
        }
        return res;

// Input: nums = [1,2,2,3,3,3], k = 2

// Output: [2,3]


        // first attempt (got stuck)
        // HashMap<Integer, Integer> box = new HashMap<>();
        // for(int i = 0; i <= nums.length; i++){
	    //     box.putIfAbsent(nums[i], box.getOrDefault(nums[i], 0) +1);
        // }
        
        // for (int key : box.keySet()) {
        //     if(key >= k){
        //         return {box.get(key)};
        //     }
        // }
        // return new int[0];
    }
}

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
       res = prefix_sum = 0 
       prefix_dict = {0 : 1}
       #prefix_dict=collections.defaultdict(int)
       #prefix_dict[0] = 1
       
       for num in nums:
        prefix_sum += num
        diff = prefix_sum - k
        #                                            #if prefix_sum - k in prefix_dict:
        res += prefix_dict.get(diff,0)                    #    res += prefix_dict[prefix_sum - k]
        prefix_dict[prefix_sum] = 1 + prefix_dict.get(prefix_sum, 0)                                                 #    prefix_dict[prefix_sum] +=1
       return res 
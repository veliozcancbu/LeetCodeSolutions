class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        half = int(len(nums) / 2)

        for i in range(half):
            result.append(nums[i])
            result.append(nums[i + half])

        return result


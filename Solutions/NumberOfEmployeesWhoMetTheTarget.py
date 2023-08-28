class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        # Compare the values belonging to the hours list with the target and add to the result
        result = 0
        for i in hours:
            if i >= target:
                result += 1

        return result
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # The "(c + extraCandies >= max(candies))" check should be performed.
        # Based on this, "True" or "False" values should be added to the "output" list.
        output = []
        max_candies = max(candies)

        for c in candies:
            if (c + extraCandies) >= max_candies:
                output.append(True)
            else:
                output.append(False)

        return output


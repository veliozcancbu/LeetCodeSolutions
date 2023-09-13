class Solution:
    def candy(self, ratings: List[int]) -> int:

        ans = [0] * len(ratings)
        minCandy = 0

        for i in range(len(ratings)):
            if ratings[i] > ratings[i - 1] and i > 0:
                ans[i] = ans[i - 1] + 1
            else:
                ans[i] = 1

        for j in reversed(range(len(ratings))):
            if j < len(ratings) - 1 and ratings[j] > ratings[j + 1]:
                ans[j] = max(ans[j], ans[j + 1] + 1)
            minCandy += ans[j]

        return minCandy

"""There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

 

Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
 

Constraints:

n == ratings.length
1 <= n <= 2 * 104
0 <= ratings[i] <= 2 * 104"""
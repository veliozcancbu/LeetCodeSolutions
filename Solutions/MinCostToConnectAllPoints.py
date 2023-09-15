from collections import defaultdict

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        dict = defaultdict(float)
        sum = 0

        for i, point in enumerate(points):
            x, y = point
            if i == 0:
                dict[(x, y)] = 0
            else:
                dict[(x, y)] = float("inf")

        while dict:
            min_value = min(dict.values())
            x, y = [key for key, value in dict.items() if value == min_value][0]
            sum += dict.pop((x, y))

            for x_, y_ in dict.keys():
                dict[(x_, y_)] = min(dict[(x_, y_)], abs(x - x_) + abs(y - y_))

        return sum

"""You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

 

Example 1:


Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation: 

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
Example 2:

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
 

Constraints:

1 <= points.length <= 1000
-106 <= xi, yi <= 106
All pairs (xi, yi) are distinct."""
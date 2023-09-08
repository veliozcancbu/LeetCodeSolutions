class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows < 0:
            return []

        output = [[1]]

        for i in range(1, numRows):
            pascal = map(lambda x, y: x + y, output[-1] + [0], [0] + output[-1])
            output.append(list(pascal))

        return output


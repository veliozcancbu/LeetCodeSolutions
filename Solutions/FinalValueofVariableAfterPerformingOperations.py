class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        for i in range(len(operations)):
            if operations[i][0] == "+" or operations [i][2] == "+":
                res += 1
            else:
                res -=1
        return res

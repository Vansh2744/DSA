class Solution:
    def findMissingNumber(self, arr):
        """
        arr: List[int] - distinct integers from 1 to n with exactly one missing.
        Returns the missing integer.
        """

        if(arr[len(arr)-1] != len(arr)+1):
            return len(arr)+1
        for i in range(len(arr)):
            if i+1 != arr[i]:
                return i+1

sol = Solution()
arr = sorted([5, 1, 3, 4])
# res = sol.findMissingNumber(arr)
# print(res)

print(arr[len(arr)-1])
print(len(arr)+1)
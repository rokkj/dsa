from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap = {} 

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevmap:
                return [prevmap[diff], i]
            prevmap[n] = i

def main():
    solution = Solution()
    print(solution.twoSum([2,4,6,8,5],6))

if __name__ == "__main__":
    main()

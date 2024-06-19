from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         hashset= set()

         for n in nums:
              if n in hashset:
                   return True
              hashset.add(n)
         return False
    
def main():
     solution = Solution()
     num = [1,2,3,4,5,6,7]
     print(solution.hasDuplicate(num))

if __name__ == "__main__":
     main()

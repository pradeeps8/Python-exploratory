
def main():
  nums = [1,2,5,3,9]
  print(twoSum(nums, 8)

def twoSum(self, nums: List[int], target: int) -> List[int]:
  diffs = {}
  for i, val in enumerate(nums):
    if (target-val) in diffs:
      return [diffs[target-val], i]
    diffs[val] = i

if __name__ == '__main__':
    main()

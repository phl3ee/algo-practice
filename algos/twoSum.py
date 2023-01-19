#def twoSum(self, nums: List[int], target: int) -> List[int]:
def twoSum(nums, target:int):
    result = []
    calc = 0
    for i in range(len(nums)):
        for j in range(len(nums[i+1:])):
            pointer = i+1+j
            print("Adding:" + str(nums[i]) + " and " + str(nums[pointer]))
            calc = nums[i] + nums[pointer]
            print("Calc is: ",calc, "Target is:",target)
            if calc == target:
                print("F YEAH!")
                result.append(i)
                result.append(pointer)
                print("Result:",result)
                return result

def twoSumFast(nums, target: int):
    numMap = dict()
    for i in range(len(nums)):
        #flip the maths in the other direction, hold the last value and index
        complement = target - nums[i]
        if complement in numMap:
            return [numMap[complement], i]
        numMap[nums[i]] = i
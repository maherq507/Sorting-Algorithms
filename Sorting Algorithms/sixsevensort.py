#Six Seven Sort
#This sort takes a list, removes all elements that aren't six or seven, and sorts the remaining elements.
class SixSevenSort:
    
    def sort(self, nums: list[any]) -> list[any]:
        snums = []
        for n in range(len(nums)):
            if nums[n] == 6 or nums[n] == 7:
                snums.append(nums[n])
        #Insertion sort remaining elements
        for i in range(len(snums) - 1):
            for j in range(len(snums) - i - 1):
                if snums[j] > snums[j + 1]:
                    temp = snums[j]
                    snums[j] = snums[j + 1]
                    snums[j + 1] = temp
        nums = snums
        return nums

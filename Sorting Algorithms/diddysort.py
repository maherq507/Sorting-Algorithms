#Diddy Sort
#This sort takes a list, removes all elements over 17, and sorts the remaining elements.
class DiddySort:
     
    def sort(self, nums: list[any]) -> list[any]:
        dnums = []
        for n in range(len(nums)):
            if nums[n] < 18:
                dnums.append(nums[n])
    #Insertion sort remaining elements
        for i in range(len(dnums) - 1):
            for j in range(len(dnums) - i - 1):
                if dnums[j] > dnums[j + 1]:
                    temp = dnums[j]
                    dnums[j] = dnums[j + 1]
                    dnums[j + 1] = temp
        nums = dnums
        return nums

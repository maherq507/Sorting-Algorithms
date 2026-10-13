#Stalin Sort
#This sort takes a list, goes through all elements, and removes any elements out of order
class StalinSort:

    def sort(self, nums: list[any]) -> list[any]:
        pointer = nums[0]
        temp = []
        temp.append(pointer)
        for n in range(1, len(nums)):
            if pointer <= nums[n]:
                temp.append(nums[n])
                pointer = nums[n]
        nums = temp
        return nums

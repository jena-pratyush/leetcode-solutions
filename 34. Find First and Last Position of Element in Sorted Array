class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binary_search(is_first):
            left, right = 0, len(nums) - 1
            index = -1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    index = mid
                    if is_first:
                        # look for earlier occurrence
                        right = mid - 1
                    else:
                        # look for later occurrence
                        left = mid + 1

                elif nums[mid] < target:
                    # remove the left side
                    left = mid + 1
                else:
                    # remove the right side
                    right = mid - 1
            return index

        first = binary_search(True)
        if first == -1:
            return [-1, -1]

        last = binary_search(False)
        return [first, last]
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return False


def test_main():

    nums1 = [1,2,3,1]
    nums2 = [1,2,3,4]
    nums3 = [1,1,1,3,3,4,3,2,4,2]

    sol = Solution()
    assert sol.containsDuplicate(nums1) == False
    assert sol.containsDuplicate(nums2) == False
    assert sol.containsDuplicate(nums3) == False

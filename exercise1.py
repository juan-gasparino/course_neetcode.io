class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if(nums[i] == nums[j]):
                    return True
            i=+1
        return False


def test_main():

    nums1 = [1,2,3,1]
    nums2 = [1,2,3,4]
    nums3 = [1,1,1,3,3,4,3,2,4,2]

    sol = Solution()
    assert sol.containsDuplicate(nums1) == True
    assert sol.containsDuplicate(nums2) == False
    assert sol.containsDuplicate(nums3) == True

def main():

    nums1 = [1,2,3,1]
    nums2 = [1,2,3,4]
    nums3 = [1,1,1,3,3,4,3,2,4,2]

    sol = Solution()
    assert sol.containsDuplicate(nums1) == True
    assert sol.containsDuplicate(nums2) == False
    assert sol.containsDuplicate(nums3) == True


if __name__ == '__main__':
    main()
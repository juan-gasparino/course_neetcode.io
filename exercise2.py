class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        i = 0
        j = 1

        while(i < len(s)):
            print(s[i])
            i = i + 1
        
        return False


def test_main():

    s1 = "anagram"
    t1 = "nagaram"

    s2 = "rat"
    t2 = "car"

    sol = Solution()
    assert sol.isAnagram(s1,t1) == True
    assert sol.isAnagram(s2,t2) == False

def main():

    s1 = "anagram"
    t1 = "nagaram"

    sol = Solution()
    sol.isAnagram(s1,t1) == True


if __name__ == '__main__':
    main()
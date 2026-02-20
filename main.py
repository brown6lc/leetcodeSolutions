class Solutions:

    # palindrome checker
    def isPalindrome(self, x: int) -> bool:
        if str(x)[::-1] == str(x):
            return True
        return False
    
    # numerical solution
    def isPalindrome(self, x: int) -> bool:
        # negative numbers and numbers ending in zero
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0

        # reverse half of the number
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # for even digits: x == reversed_half
        # for odd digits: x == reversed_half // 10
        return x == reversed_half or x == reversed_half // 10

    # roman numeral to int
    def romanToInt(self, s: str) -> int:
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        n = 0

        for i in range(len(s)):
            if i + 1 < len(s) and d[s[i]] < d[s[i + 1]]:
                n -= d[s[i]]
            else:
                n += d[s[i]]
                
        return n

    # search insert
    def searchInsert(self, nums: List[int], target: int) -> int:
            low = 0
            high = len(nums) - 1
    
            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
    
            return low



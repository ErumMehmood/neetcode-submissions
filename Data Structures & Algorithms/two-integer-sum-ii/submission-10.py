class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        f = 0
        l = len(numbers) - 1
        while f<l:
            m = (f+l)//2
            remaining = target - numbers[f]
            if numbers[f] + numbers[m] == target:
                # sum found
                return [f+1, m+1]
            elif numbers[f] + numbers[l] == target:
                # sum found
                return [f+1, l+1]  
                  
            elif remaining < numbers[m]:
                # second number is in first half array
                # call binary search for first half
                s = self.binarySearch(numbers, f, m-1, remaining)
                if  s != -1:
                    # second element found
                    return [f+1, s+1]
                else:
                    f += 1
            elif remaining > numbers[m]:
                # second number is in second half of array
                # call binary search for second half
                s = self.binarySearch(numbers, m+1, l, remaining)
                if s != -1:
                    # second element found
                    return [f+1, s+1]
                else:
                    f += 1
        return [-1, -1]        

        
    def binarySearch(self, numbers: List[int], f: int, l: int, remaining: int) -> int:
        # Base case: value not found
        if f > l:
            return -1

        m = (f + l) // 2

        # If middle element is the required value
        if numbers[m] == remaining:
            return m

        # Search left half
        elif remaining < numbers[m]:
            return self.binarySearch(numbers, f, m - 1, remaining)

        # Search right half
        else:
            return self.binarySearch(numbers, m + 1, l, remaining)
        
        
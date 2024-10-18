def countNiceSubarrays(nums, k):
    def atMostK(nums, k):
        count = 0
        left = 0
        odd_count = 0

        for right in range(len(nums)):
            if nums[right] % 2 != 0:
                odd_count += 1

            while odd_count > k:
                if nums[left] % 2 != 0:
                    odd_count -= 1
                left += 1

            count += right - left + 1

        return count

    
    return atMostK(nums, k) - atMostK(nums, k - 1)


nums = [1, 1, 2, 1, 1]
k = 3
print(countNiceSubarrays(nums, k))  

Problem 01. Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
a. 1 <= nums.length <= 10^4
b. -2^31 <= nums[i] <= 2^31 - 1

#Note: Create a GitHub file for the solution and add the file link the the answer section below.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Solution:- 
----------
  def move_zeroes(nums):
      i = 0  # Pointer to traverse the array
      j = 0  # Pointer to track the position for non-zero elements

      # Move non-zero elements to the beginning
      while i < len(nums):
          if nums[i] != 0:
              nums[i], nums[j] = nums[j], nums[i]
              j += 1
          i += 1

      # Fill the remaining elements with zeros
      while j < len(nums):
          nums[j] = 0
          j += 1

  # Test the function
  nums = [0, 1, 0, 3, 12]
  moveZeroes(nums)
  print(nums)
  # Output: [1, 3, 12, 0, 0]
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Question 02:- 
-------------- 
 First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1

Constraints:
a. 1 <= s.length <= 10^5
b. s consists of only lowercase English letters.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
Solution :-
------------  
  def firstUniqChar(s):
    char_count = {}  # Dictionary to store character frequencies

    # Update character frequencies
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the first non-repeating character
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i

    return -1

  # Test the function
  s = "leetcode"
  print(firstUniqChar(s))  # Output: 0

  s = "loveleetcode"
  print(firstUniqChar(s))  # Output: 2

  s = "aabb"
  print(firstUniqChar(s))  # Output: -1

  
  

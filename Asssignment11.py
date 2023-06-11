**Question 2**

A peak element is an element that is strictly greater than its neighbors.

Given a **0-indexed** integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to **any of the peaks**.

You may imagine that `nums[-1] = nums[n] = -∞`. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in `O(log n)` time.

**Example 1:**

```
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
```

**Example 2:**

--Solution---

def find_peak_element(list1):
    start = 0
    end = len(list1)-1
    mid = start + (end-start)//2

    while (start<=end):
        if start ==end: # if start and and index will be the same.
            return start 
        if (mid+1 < len(list1) and  list1[mid]> list1[mid+1]):
            return mid
        elif (mid-1>= 0 and list1[mid-1]> list1[mid]):
            return mid-1

        if list1[start]>=list1[mid]:
             end = mid-1
        else:
            start = mid+1
        mid = start + (end-start)//2
    return -1      



list1 = [1,2,1,3,5,6,4]
print(find_peak_element(list1))

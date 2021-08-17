from typing import Hashable, List
def nextGreat(nums1:List[int],nums2:List[int]) -> List[int]:
    """
    >>> nextGreat([4, 1, 2], [1, 3, 4, 2])
    [-1, 3, -1]
    """
    dt = {k:v for v,k in enumerate(nums2)}
    res = []
    for i in range(len(nums1)):
        next_great = -1
        next_great_index = dt[nums1[i]] + 1
        if next_great_index > len(nums2):
            res.appen(-1)
            continue
        for j in range(next_great_index, len(nums2)):
            if nums2[j] > nums1[i]:
                next_great = nums2[j]
                break
        res.append(next_great)
    return res

def nextGreatStack(nums1:List[int],nums2:List[int]) -> List[int]:
    """
    >>> nextGreatStack([4, 1, 2], [1, 3, 4, 2])
    [-1, 3, -1]
    """
    mem = {}
    stack = []
    for n in nums2:
        while len(stack) != 0 and n > stack[-1]:
            mem[stack.pop()] = n
        stack.append(n)
    return [mem[n] if n in mem else -1 for n in nums1]


if __name__ == "__main__":
    from doctest import testmod
    testmod()
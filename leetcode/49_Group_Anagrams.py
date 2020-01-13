# Given an array of strings, group anagrams together.
# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:

# All inputs will be in lowercase.
# The order of your output does not matter.
from collections import defaultdict
def solve(words):
    """
    solve(["eat", "tea", "tan", "ate", "nat", "bat"])
    >>> [["ate","eat","tea"], ["nat","tan"], ["bat"]]
    """
    result = defaultdict(list)
    for s in words:
        result[tuple(sorted(s))].append(s)
    print(result.values())

if __name__ == "__main__":
    from doctest import testmod
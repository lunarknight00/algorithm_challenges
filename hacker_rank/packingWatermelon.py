# Packing Melons Two assembly lines, one with watermelons, one with boxes. 
# Put as many watermelons into boxes as possible. You can pick where you start 
# taking watermelons from, but once you start, all melons going past you must be placed, 
# or you must stop. Calculate how many watermelons can be placed. A watermelon will fit 
# into a box with a size >= melon size. You can hold onto the melon and skip a box to place 
# in in a later one.
def melon_count(boxes,melons):
    """
    >>> melon_count([2,1,2,2],[2,3,2])
    2
    """
    boxes.sort()
    melons.sort()
    i = 0
    j = 0
    while i != len(boxes) and j != len(melons):
        if boxes[i] >= melons[j]:
            i = i + 1
            j = j +1
        else:
            i = i+1
    return j

if __name__ == "__main__":
    import doctest
    doctest.testmod()
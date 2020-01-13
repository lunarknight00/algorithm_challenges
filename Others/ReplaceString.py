    # Given a list of strings and a target string, 
    # return all strings that are off by exactly 1 character. 
    # (ex target: hello , list = [hellop, helo, he4llo, he34llo] -> hellop, helo, he4llo


def solve(target, strings):
    """

    solve("hello", ["hellop", "asajhvfdjha","helo", "he4llo", "he34llo"])
    >>> hellop, helo, he4llo

    """
    result = list()
    word = set([s for s in target])
    for s in strings:
        if len(set([c for c in s]) - word) == 1:
            result.append(s)
    print(",".join(result))
        
if __name__ == "__main__":
    from doctest import testmod


    
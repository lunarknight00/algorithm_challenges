from collections import Counter

def high_card(hand):
    """
    This function will return the
    value of highest valued card in the
    given hand
    Example: ['5', '6', 'A', 'J'] => 14('A')
    """
    highest = 0
    for i in hand:
        if i > highest:
            highest = i
    return highest

def number_of_pairs(l):
    """
    This function will return the number of pairs
    a given hand has. Also 1 is added to the
    pairs according to the priority list.
    Example: ['5','5','7','6','3'] => 2(one pair)
    ['5','5','6','6','7'] => 3(two pairs)
    ['4','3','Q','K','T'] => 0
    """
    count = Counter(l) - Counter(set(l))
    pairs = 0
    for i in count:
        if count[i] == 1:
            pairs += 1
    if pairs:
        return pairs + 1
    return 0


def three_of_a_kind(l):
    """
    This function will return 4 if
    there are three cards of same value.
    Returning of 4 is according to priority list.
    Example: ['5','5','5','T','Q'] => 4
    ['5', '7', 'Q', 'T', 'K'] => 0
    """
    count = Counter(l) - Counter(set(l))
    for i in count:
        if count[i] == 2:
            return 4
    return 0

def paired_number(l):
    """
    This function will return largest number, if
    there is a pair in the hand. The number returned
    will be in the format of high_card function
    Example: ['5', '5', '6', '7', 'K'] => 5
    ['K', 'K', 'T', 'T', '8'] => 13
    """
    repeated = (Counter(l) - Counter(set(l))).keys()
    rating = {i:i for i in range(10)}
    highest = 0
    for i in repeated:
        if rating[i] > highest:
            highest = rating[i]
    return highest

def p1_win_count(hands):
    """
    >>> p1_win_count([[7,4,2,6,5,3],[8,8,2,7,4,2]])
    2
    """
    player1 = 0
    for hand in hands:
        p1v = hand[:3]
        p2v = hand[3:]
        # number of times player 1 wins
        # score of player 1
        p1 = 0
        # score of player 2
        p2 = 0
        # flag for checking the paired cards
        flag = False
        # conditions for player 1
        if number_of_pairs(p1v):
            p1 = number_of_pairs(p1v)
            flag = True
        if three_of_a_kind(p1v):
            p1 = three_of_a_kind(p1v)
            flag = True
        # conditions for player 2
        if number_of_pairs(p2v):
            p2 = number_of_pairs(p2v)
            flag = True
        if three_of_a_kind(p2v):
            p2 = three_of_a_kind(p2v)
            flag = True
        # score more for player 1
        if p1 > p2:
            player1 += 1
        # both players same score
        elif p1 == p2:
            # cards having pairs
            if flag:
                # condition with highest in a pair
                if paired_number(p1v) > paired_number(p2v):
                    player1 += 1
                # condition with equal highest in a pair
                elif paired_number(p1v) == paired_number(p2v):
                    if high_card(p1v) > high_card(p2v):
                        player1 += 1
            # cards not having pairs
            else:
                if high_card(p1v) > high_card(p2v):
                    player1 += 1
    return player1

if __name__ == "__main__":
    import doctest
    doctest.testmod()
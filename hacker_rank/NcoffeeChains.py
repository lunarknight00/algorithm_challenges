# N coffee chains are competing for market share by a fierce advertising battle. each day a percentage of customers will be convinced to switch from one chain to another. Current market share and daily probability of customer switching is given. If the advertising runs forever, what will be the final distribution of market share?

# Assumption: N is an integer less than 25, Total market share is 1.0, probability that a customer switches is independent of other customers and days.

# Example: 2 coffee chains: A and B
# market share of A: 0.4
# market share of B: 0.6
# Each day, there is a 0.2 probability that a customer switches from A to B
# Each day, there is a 0.1 probability that a customer switches from B to A
# input: market_share=[0.4,0.6], switch_prob = [[.8,.2][.1,.9]]
# output: [0.3333 0.6667]

import numpy as np
def NCoffeChains(market_share,switch_prob):
    """
    >>> NCoffeChains([0.4,0.6],[[0.8,0.2],[0.1,0.9]])
    [0.3333, 0.6667]
    """
    np.set_printoptions(precision=4)  
    pn = np.array(switch_prob)
    while True:
        curr = pn
        pn = np.dot(switch_prob,pn)
        if np.array_equal(curr,pn):
            break
    return np.round(np.dot(market_share, pn),decimals = 4).tolist()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
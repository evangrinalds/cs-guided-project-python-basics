"""
In a city-state of n people, there is a rumor going around that one of the n people is a spy for the neighboring city-state.

The spy, if it exists:

Does not trust anyone else.
Is trusted by everyone else (he's good at his job).
Works alone; there are no other spies in the city-state.
You are given a list of pairs, trust. Each trust[i] = [a, b] represents the fact that person a trusts person b.

If the spy exists and can be found, return their identifier. Otherwise, return -1.
""""

"""
Understand
input: n = 2, trust = [[1, 2]]
output: 2

Plan
1. define count
2. iterate thru variables i, j in trust
3. iterate thru range
4. if not return -1 
"""

def uncover_spy(n, trust):
    count = [0] * (n + 1)
    for i, j in trust:
        count[i] -= 1
        count[j] += 1
    for i in range(1, n + 1):
        if count[i] == n - 1:
            return i
    return -1

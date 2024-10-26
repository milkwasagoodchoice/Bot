from typing import List, Tuple


def find_sum(target: int, li: List[int]) -> Tuple[int, int]:

    n = len(li)
    for i in range(n):
        for j in range(i + 1, n):
            if li[i] + li[j] == target:
                return (i, j)
    return (-1, -1)


def find_sum_fast(target: int, li: List[int]) -> Tuple[int, int]:

    seen = {}
    for i, num in enumerate(li):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i
    return (-1, -1)  

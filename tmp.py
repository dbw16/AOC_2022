from typing import List
from collections import Counter
from functools import cache
import itertools

for is_even, value in itertools.groupby([1,2,3,4], key=lambda x: x % 2 == 0):
    print(is_even)
    for word in value:
        print(word)

@cache
def match(current: str, next: str):
    if len(next) - 1 != len(current):
        return False

    current_index = 0
    next_index = 0
    for _ in range(len(current)):
        if current[current_index] != next[next_index]:
            if current_index != next_index:  # we already have a miss match
                return False
            else:
                next_index += 1
        next_index += 1
        current_index += 1
    return True

from collections import defaultdict

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort()
        words.sort(key=len)
        words_split_by_len = defaultdict(list)

        for word in words:
            words_split_by_len[len(word)].append(word)

        max_found = 1
        current = 1
        for word in words:
            while next_word:
                if words_split_by_len.get(len(word) + 1):
                    for possible_next in words_split_by_len.get(len(word) + 1):
                        if not match(word, possible_next):
                            max_found = max(max_found, current)
                        else:
                            current += 1

        print(words_split_by_len)


print(Solution().longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"]))

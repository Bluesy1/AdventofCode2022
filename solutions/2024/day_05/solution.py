# puzzle prompt: https://adventofcode.com/2024/day/5

from ...base import TextSolution, answer
from ...utils.tools import *


class Solution(TextSolution):
    _year = 2024
    _day = 5

    @answer((5747, 5502))
    def solve(self) -> tuple[int, int]:
        orders, pages = self.input.split("\n\n")
        must_after = defaultdict(set)
        for ordering in orders.splitlines():
            before, after = ordering.split("|")
            must_after[after].add(before)
        part1 = part2 = 0
        for group_ in pages.splitlines():
            group = deque(group_.split(","))
            group_set = set(group)
            valid = True
            pages = set()
            for i, page in enumerate(group):
                pages.add(page)
                for before in must_after[page] & group_set:
                    if before not in pages:
                        valid = False
                        break
                else:
                    continue
                break
            if valid:
                part1 += int(group[len(group) // 2])
            else:
                while not valid:
                    group.remove(before)
                    group.insert(i, before)
                    valid = True
                    pages = set()
                    for i, page in enumerate(group):
                        pages.add(page)
                        for before in must_after[page] & group_set:
                            if before not in pages:
                                valid = False
                                break
                        else:
                            continue
                        break
                part2 += int(group[len(group) // 2])

        return part1, part2

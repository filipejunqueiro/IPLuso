from typing import Optional, TypeVar

T = TypeVar("T", int, float, str)

class Search:
    @staticmethod
    def Linear(target_list: list[T], target_value: T, count_comparisons: bool) -> tuple[bool, Optional[int]]:
        comparisons = 0
        for value in target_list:
            if count_comparisons:
                    comparisons += 1
            if value == target_value:
                return (True, comparisons if count_comparisons else None)
            
        return (False, comparisons if count_comparisons else None)

    # O(log n) | Ω(1) | Θ(log n)
    @staticmethod
    def Binary(target_list: list[T], target_value: T, count_comparisons: bool) -> tuple[bool, Optional[int]]:
        start = 0
        end = target_list.__len__() - 1
        comparisons = 0

        while start <= end:
            middle = (start + end) >> 1
            current_value = target_list[middle]

            if current_value == target_value:
                comparisons += 1
                return (True, comparisons if count_comparisons else None)

            if current_value < target_value:
                comparisons += 1
                start = middle + 1
            else:
                comparisons += 1
                end = middle - 1

        return (False, comparisons if count_comparisons else None)
from typing import Literal

VALID_TYPES = (int, float)
SUCCESS = tuple[Literal[True], int | float]
ERROR = tuple[Literal[False], str]
RESULT = SUCCESS | ERROR

class Sum:
    @staticmethod
    def with_range(start: int | float, end: int | float) -> RESULT:
        start_t = type(start)
        end_t = type(end)

        if start_t not in VALID_TYPES or end_t not in VALID_TYPES:
            return (False, "start and end values must be both one of the following datatype: int or float")

        if start_t is not end_t:
            return (False, "start and end values aren't using the same datatype.")
        
        if start >= end:
            return (False, "the start value should always be smaller than the end value.")

        total = (start + end) * (end - start + 1)

        if start_t is int:
            return (True, total // 2)
        
        return (True, total / 2)
    
    @staticmethod
    def to_value(value: int | float) -> RESULT:
        zero = type(value)(0)
        return Sum.with_range(zero, value)
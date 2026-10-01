from typing import Literal

ValidType = (int, float)
Success = tuple[Literal[True], int | float]
Error = tuple[Literal[False], str]
Result = Success | Error

class Sum:
    @staticmethod
    def WithRange(start: int | float, end: int | float) -> Result:
        start_t = type(start)
        end_t = type(end)

        if start_t not in ValidType or end_t not in ValidType:
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
    def ToValue(value: int | float) -> Result:
        zero = type(value)(0)
        return Sum.WithRange(zero, value)
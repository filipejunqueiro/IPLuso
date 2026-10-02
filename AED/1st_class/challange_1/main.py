from sum import Sum
from utils import Utils

S = Sum()
U = Utils()

def main() -> None:
    start = U.input_number("start: ")
    end = U.input_number("end: ")
    success, result = S.with_range(start, end)
    print(success, result)

    U.clear_screen(False)

    value = U.input_number("value: ")
    success, result = S.to_value(value)
    print(success, result)

main()
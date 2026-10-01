from sum import Sum as S
from utils import Utils as U

def main() -> None:
    start = U.InputNumber("start: ",)
    end = U.InputNumber("end: ")
    success, result = S.WithRange(start, end)
    print(success, result)

    U.ClearScreen(False)

    value = U.InputNumber("value: ")
    success, result = S.ToValue(value)
    print(success, result)

main()
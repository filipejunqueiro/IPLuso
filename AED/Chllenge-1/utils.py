from os import system as Exec
from platform import system as Sys 

class Utils:
    @staticmethod
    def ParseNumber(string: str) -> int | float:
        string = string.strip()
        try:
            return int(string)
        except ValueError:
            return float(string)

    @staticmethod
    def ClearScreen(now = True) -> None:
        if not now:
            input("Press any key to continue...")

        Exec("cls" if Sys() == "Windows" else "clear")

    @staticmethod
    def InputNumber(message: str, clear: bool = False) -> int | float:
        while True:
            if clear:
                Utils.ClearScreen()
            try:
                user_input = input(message)
                return Utils.ParseNumber(user_input)
            except (ValueError, EOFError):
                continue
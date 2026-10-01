from os import system as cmd
from platform import system as sys 

class Utils:
    @staticmethod
    def clear_screen(now = True) -> None:
        if not now:
            input("Press any key to continue...")

        cmd("cls" if sys() == "Windows" else "clear")

    @staticmethod
    def parse_number(string: str) -> int | float:
        string = string.strip()
        try:
            return int(string)
        except ValueError:
            return float(string)

    @staticmethod
    def input_number(message: str, clear: bool = False) -> int | float:
        while True:
            if clear:
                Utils.clear_screen()         
            try:
                user_input = input(message)
                return Utils.parse_number(user_input)
            except (ValueError, EOFError):
                continue
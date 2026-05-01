from tkinter import *


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("CALCULATOR")
        self.root.configure(background="black")
        self.root.geometry("280x430")
        self.root.resizable(0, 0)

        self.first_number = None
        self.operator = None
        self.reset_next = False  

        self.build_ui()


    def build_ui(self):
        self.result_var = StringVar(value="0")
        result_label = Label(
            self.root,
            textvariable=self.result_var,
            bg="black", fg="white",
            font=("Verdana", 30),
            anchor="e",
        )

        result_label.grid(
            row=0, column=0, columnspan=4,
            pady=(50, 25), padx=10, sticky="ew",
        )

        buttons = [
            ("7", 1, 0, 1, lambda: self.press_digit("7")),
            ("8", 1, 1, 1, lambda: self.press_digit("8")),
            ("9", 1, 2, 1, lambda: self.press_digit("9")),
            ("/", 1, 3, 1, lambda: self.press_operator("/")),

            ("4", 2, 0, 1, lambda: self.press_digit("4")),
            ("5", 2, 1, 1, lambda: self.press_digit("5")),
            ("6", 2, 2, 1, lambda: self.press_digit("6")),
            ("*", 2, 3, 1, lambda: self.press_operator("*")),

            ("1", 3, 0, 1, lambda: self.press_digit("1")),
            ("2", 3, 1, 1, lambda: self.press_digit("2")),
            ("3", 3, 2, 1, lambda: self.press_digit("3")),
            ("-", 3, 3, 1, lambda: self.press_operator("-")),

            ("C",  4, 0, 1, self.clear),
            ("0",  4, 1, 1, lambda: self.press_digit("0")),
            (".",  4, 2, 1, self.press_decimal),
            ("+",  4, 3, 1, lambda: self.press_operator("+")),

            ("=",  5, 0, 4, self.calculate),
        ]

        for (text, row, col, span, cmd) in buttons:
            btn = Button(
                self.root,
                text=text,
                bg="#808080", fg="white",
                width=5, height=2,
                font=("Verdana", 14),
                command=cmd,
            )
            
            btn.grid(row=row, column=col, columnspan=span, sticky="ew")

    def get_display(self) -> str:
        return self.result_var.get()

    def set_display(self, value: str):
        self.result_var.set(value)

    def press_digit(self, digit: str):
        current = self.get_display()
        if self.reset_next or current == "0":
            self.set_display(digit)
            self.reset_next = False
        else:
            self.set_display(current + digit)

    def press_decimal(self):
        current = self.get_display()
        if self.reset_next:
            self.set_display("0.")
            self.reset_next = False
        elif "." not in current:
            self.set_display(current + ".")

    def press_operator(self, op: str):
        if self.first_number is not None and not self.reset_next:
            self.calculate()

        raw = self.get_display()
        if raw in ("", "Error"):
            return

        self.first_number = float(raw)
        self.operator = op
        self.reset_next = True  

    def calculate(self):
        if self.first_number is None or self.operator is None:
            return

        raw = self.get_display()
        if raw in ("", "Error"):
            return

        second = float(raw)

        try:
            if self.operator == "+":
                result = self.first_number + second
            elif self.operator == "-":
                result = self.first_number - second
            elif self.operator == "*":
                result = self.first_number * second
            elif self.operator == "/":
                if second == 0:
                    raise ZeroDivisionError
                result = self.first_number / second
            else:
                return

            self.set_display(
                str(int(result)) if result == int(result) else str(result)
            )
        except ZeroDivisionError:
            self.set_display("Error")
        finally:
            self.first_number = None
            self.operator = None
            self.reset_next = True

    def clear(self):
        self.set_display("0")
        self.first_number = None
        self.operator = None
        self.reset_next = False


def main():
    root = Tk()
    Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
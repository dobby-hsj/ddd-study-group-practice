class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

if __name__ == "__main__":
    calc = Calculator()
    print(f"1 + 2 = {calc.add(1, 2)}")
    print(f"5 - 3 = {calc.subtract(5, 3)}")


test 12314 fwfwfwfwfwfwfwfwfwfwefasdfasd
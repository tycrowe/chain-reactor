class Calculator:
    def __init__(self, input_number: int):
        self.input_number = input_number

    def add(self, number: int) -> 'Calculator':
        self.input_number += number
        return self

    def subtract(self, number: int) -> 'Calculator':
        self.input_number -= number
        return self

    def multiply(self, number: int) -> 'Calculator':
        self.input_number *= number
        return self

    def divide(self, number: int) -> 'Calculator':
        self.input_number /= number
        return self

    def result(self) -> int:
        return self.input_number


if __name__ == '__main__':
    final = Calculator(10).add(5).subtract(3).multiply(2).divide(4).result()
    print(final)
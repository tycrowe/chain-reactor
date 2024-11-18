from enum import Enum


class CalculatorEnum(Enum):
    ADD = 1
    SUBTRACT = 2
    MULTIPLY = 3
    DIVIDE = 4


class CalculatorAction:
    def __init__(self, action: CalculatorEnum, number: int, result: int):
        self.action = action
        self.number = number
        self.result = result

    def __str__(self):
        return f"{self.action.name}: {self.number} = {self.result}"


class Calculator:
    def __init__(self, input_number: int):
        self.input_number = input_number
        self.calculation_history = []
        self.memory = 0

    def mem(self) -> 'Calculator':
        self.memory = self.input_number
        return self

    def mem_clear(self) -> 'Calculator':
        self.memory = 0
        return self

    def mem_recall(self) -> 'Calculator':
        self.input_number = self.memory
        return self

    def add(self, numbers) -> 'Calculator':
        if isinstance(numbers, list):
            for number in numbers:
                self.input_number += number
                self.calculation_history.append(CalculatorAction(CalculatorEnum.ADD, number, self.input_number))
        else:
            self.input_number += numbers
            self.calculation_history.append(CalculatorAction(CalculatorEnum.ADD, numbers, self.input_number))
        return self

    def subtract(self, numbers) -> 'Calculator':
        if isinstance(numbers, list):
            for number in numbers:
                self.input_number -= number
                self.calculation_history.append(CalculatorAction(CalculatorEnum.SUBTRACT, number, self.input_number))
        else:
            self.input_number -= numbers
            self.calculation_history.append(CalculatorAction(CalculatorEnum.SUBTRACT, numbers, self.input_number))
        return self

    def multiply(self, numbers) -> 'Calculator':
        if isinstance(numbers, list):
            for number in numbers:
                self.input_number *= number
                self.calculation_history.append(CalculatorAction(CalculatorEnum.MULTIPLY, number, self.input_number))
        else:
            self.input_number *= numbers
            self.calculation_history.append(CalculatorAction(CalculatorEnum.MULTIPLY, numbers, self.input_number))
        return self

    def divide(self, numbers) -> 'Calculator':
        if isinstance(numbers, list):
            for number in numbers:
                if number == 0:
                    raise ValueError("Cannot divide by zero")
                self.input_number /= number
                self.calculation_history.append(CalculatorAction(CalculatorEnum.DIVIDE, number, self.input_number))
        else:
            if numbers == 0:
                raise ValueError("Cannot divide by zero")
            self.input_number /= numbers
            self.calculation_history.append(CalculatorAction(CalculatorEnum.DIVIDE, numbers, self.input_number))
        return self

    def undo(self, count) -> 'Calculator':
        for _ in range(count):
            if len(self.calculation_history) == 0:
                break
            last_action = self.calculation_history.pop()
            print(f"Undo: {last_action}")
            if last_action.action == CalculatorEnum.ADD:
                self.input_number -= last_action.number
            elif last_action.action == CalculatorEnum.SUBTRACT:
                self.input_number += last_action.number
            elif last_action.action == CalculatorEnum.MULTIPLY:
                self.input_number /= last_action.number
            elif last_action.action == CalculatorEnum.DIVIDE:
                self.input_number *= last_action.number
        print(f"Undo complete, value now: {self.input_number}")
        return self

    def reset(self) -> 'Calculator':
        self.input_number = 0
        self.calculation_history = []
        return self

    def print_history(self) -> 'Calculator':
        for action in self.calculation_history:
            print(action)
        return self

    def result(self) -> int:
        return self.input_number


if __name__ == '__main__':
    try:
        final = Calculator(10).add([5, 10]).add([100, 1]).print_history().undo(3).multiply([2, 3, 5]).print_history().result()
        print(final)
    except ValueError as e:
        print(e)
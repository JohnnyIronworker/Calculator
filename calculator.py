"""
Calculator module for performing basic arithmetic operations.
"""

class Calculator:
    """
    Calculator class for performing basic arithmetic operations.
    """

    def __init__(self, op1: float, op2: float):
        """
        Initialization of the 2 operands

        :param op1: first operand
        :param op2: second operand
        """
        self._op1 = op1
        self._op2 = op2

    def sum(self) -> float:
        """
        Return sum product of two operands.
        """
        return self._op1 + self._op2

    def subtract(self) -> float:
        """
        Return subtract product of two operands.
        """
        return self._op1 - self._op2

    def multiply(self) -> float:
        """
        Return multiplied product of two operands.
        """
        return self._op1 * self._op2

    def divide(self) -> float:
        """
        Return divided product of two operands.
        """
        if self._op2 == 0:
            raise ValueError("This is impossible to divide by zero!")
        return self._op1 / self._op2

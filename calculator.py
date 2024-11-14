"""
Calculator module for performing basic arithmetic operations.
"""

class Calculator:
    """
    Klasa Calculator służy do wykonywania podstawowych operacji arytmetycznych:
    dodawanie, odejmowanie, mnożenie i dzielenie.
    """

    def __init__(self, op1: float, op2: float):
        """
        Inicjalizuje dwa operandy.

        :param op1: pierwszy operand
        :param op2: drugi operand
        """
        self._op1 = op1
        self._op2 = op2

    def sum(self) -> float:
        """
        Zwraca sumę dwóch operandów.
        """
        return self._op1 + self._op2

    def subtract(self) -> float:
        """
        Zwraca różnicę dwóch operandów.
        """
        return self._op1 - self._op2

    def multiply(self) -> float:
        """
        Zwraca iloczyn dwóch operandów.
        """
        return self._op1 * self._op2

    def divide(self) -> float:
        """
        Zwraca iloraz dwóch operandów. Zgłasza błąd przy dzieleniu przez zero.
        """
        if self._op2 == 0:
            raise ValueError("Nie można dzielić przez zero")
        return self._op1 / self._op2

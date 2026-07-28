import operator
from collections.abc import Callable

from calculadora.excepciones import (
    ErrorDivisionEntreCero,
    ErrorOperacionNoSoportada
)
from calculadora.operaciones.base import Operacion


Numero = int | float


class OperacionAritmetica(Operacion):
    """Implementa las operacions aritméticas básicas."""

    _OPERACIONES: dict[str, Callable[[Numero, Numero], Numero]] = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }

    def admite(self, operador: str) -> bool:
        """Indica si la operacion es una operación aritmética admitida."""
        return operador in self._OPERACIONES

    def ejecutar(
            self,
            operando_izquierdo: Numero,
            operando_derecho: Numero,
            operador: str) -> Numero:
        """Ejecuta la operacion aritmética solicitada."""

        if not self.admite(operador):
            raise ErrorOperacionNoSoportada(f"El operador '{operador}' no es una operación aritmética admitida.")

        if operador == "/" and operando_derecho == 0:
            raise ErrorDivisionEntreCero("No es posible dividir entre cero.")

        operacion = self._OPERACIONES[operador]

        return operacion(operando_izquierdo, operando_derecho)
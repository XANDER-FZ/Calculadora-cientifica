from abc import ABC, abstractmethod

class Operacion(ABC):
    """Clase base abstracta para las operaciones de la calculadora."""

    @abstractmethod
    def admite(self, operador: str) -> bool:
        """
        Indica si la operación admite el operador recibido.
        
        Args:
            operador: Símbolo que representa la operación.

        Returns:
            True si el operador es admitido; caso contrario, False.
        """
        ...

    @abstractmethod
    def ejecutar(
            self,
            operando_izquierdo: int | float,
            operando_derecho: int | float,
            operador: str
    ) -> int | float:
        """
        Ejecuta una operacion entre dos operandos.
        
        Args:
            operando_izquierdo: Primer número de la operación.
            operando_derecho: Segundo número de la operación.
            operador: Símbolo de la operación solicitada.

        Returns:
            El resultado numérico de la operación.
        """
        ...
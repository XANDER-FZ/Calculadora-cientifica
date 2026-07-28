"""Excepciones propias del dominio de la calculadora."""

class ErrorCalculadora(Exception):
    """Excepción base para todos los errores de la calculadora."""


class ErrorOperandoInvalido(ErrorCalculadora):
    """Se produce cuando uno de los operando no es válido."""


class ErrorOperacionNoSoportada(ErrorCalculadora):
    """Se produce cuando el operador solicitado no está disponible."""


class ErrorDivisionEntreCero(ErrorCalculadora):
    """Se produce cuando se intenta dividir entre cero."""


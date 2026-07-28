import pytest

from calculadora.excepciones import (
    ErrorDivisionEntreCero,
    ErrorOperacionNoSoportada
)
from calculadora.operaciones.aritmetica import OperacionAritmetica


@pytest.mark.parametrize("operador", ["+", "-", "*", "/"])
def test_admite_operadores_aritmeticos(operador: str) -> None:
    operacion = OperacionAritmetica()

    resultado = operacion.admite(operador)

    assert resultado is True


@pytest.mark.parametrize("operador", ["%", "^", "//", ""])
def test_no_admite_operadores_desconocidos(operador: str) -> None:
    operacion = OperacionAritmetica()

    resultado = operacion.admite(operador)

    assert resultado is False


@pytest.mark.parametrize(
    "operando_izquierdo, operando_derecho, operador, resultado_esperado",
    [
        (10, 2, "+", 12),
        (10, 2, "-", 8),
        (10, 2, "*", 20),
        (10, 2, "/", 5.0),
        (-4, 2, "+", -2),
        (2.5, 2, "*", 5.0),
        (0, 5, "/", 0.0)
    ]
)
def test_ejecutar_operaciones_aritmeticas(
    operando_izquierdo: int | float,
    operando_derecho: int | float,
    operador: str,
    resultado_esperado: int | float
) -> None:
    operacion = OperacionAritmetica()

    resultado = operacion.ejecutar(
        operando_izquierdo,
        operando_derecho,
        operador
    )

    assert resultado == resultado_esperado


def test_division_entre_cero_lanza_excepcion() -> None:
    operacion = OperacionAritmetica()

    with pytest.raises(
        ErrorDivisionEntreCero,
        match="No es posible dividir entre cero"
    ):
        operacion.ejecutar(10, 0, "/")


def test_operador_no_soportado_lanza_excepcion() -> None:
    operacion = OperacionAritmetica()

    with pytest.raises(
        ErrorOperacionNoSoportada,
        match="no es una operación aritmética admitida"
    ):
        operacion.ejecutar(10, 2, "%")

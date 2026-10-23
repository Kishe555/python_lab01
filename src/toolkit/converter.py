from math import isfinite
from .errors import (ToolkitError,
                                Unknown_Unit_Error,
                                Invalid_Temperature_Error,
                                Incompatible_Units_Error)

#коэффициенты перевода единиц длины массы и обозначение температурных шкал
length = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1.0,
    "km": 1000.0, }

mass = {
    "g": 0.001,
    "kg": 1.0, }

temperature = {"c", "f", "k"}

#сначала проверяет с чем имеет дело потом переводит длину массу или температуру
def convert(value: float, unit1: str, unit2: str) -> float:
    unit1 = unit1.lower()
    unit2 = unit2.lower()

    try:
        value = float(value)
    except ValueError:
        raise ToolkitError("неверное числовое значение") from None

    for unit in (unit1, unit2):
        if unit not in length and unit not in mass and unit not in temperature:
            raise Unknown_Unit_Error("Неизвестная единица")


    if unit1 in length and unit2 in length:
        return value * length[unit1] / length[unit2]

    if unit1 in mass and unit2 in mass:
        return value * mass[unit1] / mass[unit2]


    if unit1 in temperature and unit2 in temperature:
        minimum = {"c": -273.15, "f": -459.67, "k": 0.0}
        if value < minimum[unit1]:
            raise Invalid_Temperature_Error("Температура ниже минимальной")

        if unit1 in "c":
            kelvin = value + 273.15
        elif unit1 in "f":
            kelvin = (value + 459.67) * 5 / 9
        else:
            kelvin = value


        if unit2 in "c":
            return kelvin - 273.15
        elif unit2 in "f":
            return (kelvin - 273.15) * 9 / 5 + 32
        else:
            return kelvin

    raise Incompatible_Units_Error("Единицы относятся к разным группам")

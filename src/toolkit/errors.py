class ToolkitError(Exception):
    """Базовая ошибка toolkit"""
    pass

class Empty_Expression_Error(ToolkitError):
    """Выражение отсутствует"""
    pass


class Invalid_Symbol_Error(ToolkitError):
    """Недопустимый символ"""
    pass


class Invalid_Expression_Error(ToolkitError):
    """Нарушена структура выражения"""
    pass


class Division_By_Zero_Error(ToolkitError):
    """Деление на ноль"""
    pass


class Unknown_Unit_Error(ToolkitError):
    """Неизвестная единица"""
    pass


class Incompatible_Units_Error(ToolkitError):
    """Разные группы величин"""
    pass


class Invalid_Temperature_Error(ToolkitError):
    """Температура ниже абсолютного нуля"""
    pass

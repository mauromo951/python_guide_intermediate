class AppError(Exception):
    """Excepción base para la aplicación."""
    pass


class DivisionByZeroError(AppError):
    """Excepción personalizada para división entre cero."""
    def __init__(self, message="No puedes dividir entre cero"):
        super().__init__(message)

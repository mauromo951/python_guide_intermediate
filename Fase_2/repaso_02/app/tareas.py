class Tarea:
    def __init__(self, titulo, completada=False):
        self.titulo = titulo
        self.completada = completada

    def marcar_completada(self):
        self.completada = True

    def __repr__(self):
        estado = "✅" if self.completada else "❌"
        return f"{estado} {self.titulo}"

class Tarea:
    """
    Clase que representa una tarea en el sistema de To-Do.
    """

    def __init__(self, id, titulo, completada=False):
        self.id = id
        self.titulo = titulo
        self.completada = completada

    def __str__(self):
        estado = "✅" if self.completada else "❌"
        return f"[{estado}] {self.titulo} (id: {self.id})"

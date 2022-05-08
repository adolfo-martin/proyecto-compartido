from dataclasses import dataclass
from datetime import date


@dataclass
class Impuesto:
    id: int
    nombre: str
    valor: float
    fecha_inicio: date
    fecha_fin: date = None

    def __repr__(self) -> str:
        return f'IMPUESTO {self.id} {self.nombre} {self.valor} {self.fecha_inicio} {self.fecha_fin}'

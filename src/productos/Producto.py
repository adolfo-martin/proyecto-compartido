from dataclasses import dataclass


@dataclass
class Producto:
    id: int
    nombre: str
    precio: float
    impuesto: int


def __repr__(self):
    return f'{self.id} {self.nombre} {self.precio} {self.impuesto}'

from dataclasses import dataclass


@dataclass
class LineaFactura:
    producto: int
    cantidad: int

    def __repr__(self) -> str:
        return f'{self.cantidad} unidades de {self.producto}'

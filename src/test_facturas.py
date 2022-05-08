from facturas.Factura import Factura
from facturas.LineaFactura import LineaFactura
from productos.Producto import Producto
from productos.Productos import Productos


def test() -> None:
    producto1 = Producto(1, 'Bolígrafo azul', 1.15, 4)
    producto2 = Producto(2, 'Pañales', 6.75, 3)
    producto3 = Producto(3, 'Galletas de chocolate', 0.95, 4)
    producto4 = Producto(4, 'Pasta de dientes', 1.70, 3)

    productos = Productos()
    productos.añadir(producto1)
    productos.añadir(producto2)
    productos.añadir(producto3)
    productos.añadir(producto4)

    lineaFactura1 = LineaFactura(1, 1)
    lineaFactura2 = LineaFactura(2, 3)
    lineaFactura3 = LineaFactura(3, 4)
    lineaFactura4 = LineaFactura(4, 2)

    factura = Factura()
    factura.establecerProductos(productos)
    factura.añadirLineaFactura(lineaFactura1)
    factura.añadirLineaFactura(lineaFactura2)
    factura.añadirLineaFactura(lineaFactura3)
    factura.añadirLineaFactura(lineaFactura4)

    print(factura)


if __name__ == '__main__':
    test()

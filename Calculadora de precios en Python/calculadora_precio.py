def dinero(n):
    """Da formato de dinero: 1234.5 -> $1,234.50"""
    return f"${n:,.2f}"


def leer_precio_e_impuesto():
    """Pide precio e impuesto en un mismo renglón, separados por espacio."""
    while True:
        entrada = input("Escribe el precio y el % de impuesto (ej: 100 7): ").split()
        try:
            if len(entrada) != 2:
                raise ValueError
            precio = float(entrada[0])
            impuesto = float(entrada[1])
            if precio < 0 or impuesto < 0:
                raise ValueError
            return precio, impuesto
        except ValueError:
            print("Entrada inválida. Escribe dos números mayores o iguales a 0.")


def leer_descuento():
    """Pide el porcentaje de descuento (entre 0 y 100)."""
    while True:
        try:
            descuento = float(input("Descuento por promoción (%): "))
            if 0 <= descuento <= 100:
                return descuento
            print("El descuento debe estar entre 0 y 100.")
        except ValueError:
            print("Entrada inválida. Escribe un número.")


def main():
    precio, impuesto = leer_precio_e_impuesto()
    descuento = leer_descuento()

    # Cálculos
    monto_impuesto = precio * impuesto / 100
    precio_con_impuesto = precio + monto_impuesto
    monto_descuento = precio_con_impuesto * descuento / 100
    precio_final = precio_con_impuesto - monto_descuento

    # Resultados
    print("\n--------- RESULTADO ---------")
    print(f"Precio de lista:         {dinero(precio):>12}")
    print(f"Impuesto ({impuesto:g}%):".ljust(25) + f"+ {dinero(monto_impuesto):>10}")
    print(f"Precio + impuesto:       {dinero(precio_con_impuesto):>12}")
    print(f"Descuento ({descuento:g}%):".ljust(25) + f"- {dinero(monto_descuento):>10}")
    print("-----------------------------")
    print(f"PRECIO A PAGAR:          {dinero(precio_final):>12}")


if __name__ == "__main__":
    main()

class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cuentas = []

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

class Cuenta:
    def __init__(self, numero, saldo, limite_credito, tipo):
        self.numero, self.saldo, self.limite_credito, self.tipo = numero, saldo, limite_credito, tipo

class Cliente:
    def __init__(self, nombre, direccion, numero_cuenta, contraseña):
        self.nombre, self.direccion, self.numero_cuenta, self.contraseña = nombre, direccion, numero_cuenta, contraseña

class Cajero:
    def __init__(self, nombre, codigo, banco):
        self.nombre, self.codigo, self.banco = nombre, codigo, banco

    def mostrar_menu(self):
        opciones = ["Retiro en efectivo", "Ingreso de efectivo", "Pago de facturas", "Transferencia", "Salir"]
        print("\n".join(f"{i + 1}. {opcion}" for i, opcion in enumerate(opciones)))

    def ejecutar_opcion(self, opcion, cliente):
        acciones = [self.retirar_efectivo, self.ingresar_efectivo, self.pagar_factura, self.transferir_fondos, None]
        if 1 <= opcion <= 4:
            acciones[opcion - 1](cliente)

    def retirar_efectivo(self, cliente):
        cuenta = self.obtener_cuenta(cliente.numero_cuenta)
        cantidad = float(input("Ingrese el monto a retirar: "))
        if 0 < cantidad <= cuenta.saldo:
            cuenta.saldo -= cantidad
            print(f"Retiro exitoso. Nuevo saldo: {cuenta.saldo}")
        else:
            print("Fondos insuficientes o cantidad no válida.")

    def ingresar_efectivo(self, cliente):
        cuenta = self.obtener_cuenta(cliente.numero_cuenta)
        cantidad = float(input("Ingrese el monto a depositar: "))
        if cantidad > 0:
            cuenta.saldo += cantidad
            print(f"Ingreso exitoso. Nuevo saldo: {cuenta.saldo}")
        else:
            print("Cantidad no válida.")

    def pagar_factura(self, cliente):
        informacion_factura = input("Ingrese la información de su factura: ")
        print("Factura pagada con éxito.")

    def transferir_fondos(self, cliente):
        cuenta_origen = self.obtener_cuenta(cliente.numero_cuenta)
        numero_cuenta_destino = int(input("Ingrese el número de cuenta del destinatario: "))
        cuenta_destino = self.obtener_cuenta(numero_cuenta_destino)

        cantidad = float(input("Ingrese el monto a transferir: "))
        if 0 < cantidad <= cuenta_origen.saldo:
            cuenta_origen.saldo -= cantidad
            cuenta_destino.saldo += cantidad
            print("Transferencia exitosa.")
        else:
            print("Fondos insuficientes o cantidad no válida.")

    def obtener_cuenta(self, numero_cuenta):
        return next((cuenta for cuenta in self.banco.cuentas if cuenta.numero == numero_cuenta), None)

def main():
    mi_banco = Banco("Banco de Esperanza")
    cuentas = [Cuenta(1, 1000, 500, "Corriente"), Cuenta(2, 500, 200, "Ahorro")]
    [mi_banco.agregar_cuenta(cuenta) for cuenta in cuentas]

    clientes = [Cliente("Jhon", "Calle 123", 1, "pass123"), Cliente("Jenny", "Calle 456", 2, "pass456")]

    cajero_automatico = Cajero("Cajero 1", "1234", mi_banco)

    numero_cuenta = int(input("Ingrese su número de cuenta: "))
    contraseña = input("Ingrese su pin de acceso: ")

    cliente_autenticado = next((cliente for cliente in clientes if cliente.numero_cuenta == numero_cuenta and cliente.contraseña == contraseña), None)

    if cliente_autenticado:
        print(f"Bienvenido, {cliente_autenticado.nombre}.")
        cuenta_autenticada = cajero_automatico.obtener_cuenta(cliente_autenticado.numero_cuenta)
        print(f"Número de cuenta: {cliente_autenticado.numero_cuenta}")
        print(f"Saldo: {cuenta_autenticada.saldo}")

        opcion = 0
        while opcion != 5:
            cajero_automatico.mostrar_menu()
            opcion = int(input("Seleccione una opción (1-5): "))
            cajero_automatico.ejecutar_opcion(opcion, cliente_autenticado)

    else:
        print("Autenticación fallida. Verifique su número de cuenta y pin de acceso.")

if __name__ == "__main__":
    main()
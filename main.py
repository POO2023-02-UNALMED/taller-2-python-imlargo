class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self, color):
        colores =  [ "rojo", "verde", "amarillo", "negro", "blanco" ]
        if (color in colores):
            self.color = color


class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
        
    def cambiarRegistro(self, registro):
        self.registro = registro
        
    def asignarTipo(self, tipo):
        if (tipo == "electrico" or tipo == "gasolina"):
            self.tipo = tipo
            

class Auto:
    cantidadCreados = 0
    
    def __init__(self, modelo, precio, asientos, marca, motor, registro, cantidadCreados):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.registro = registro
        self.motor = motor
        Auto.cantidadCreados = cantidadCreados
    
    def cantidadAsientos(self):
        contador = 0
        for asiento in self.asientos:
            if (isinstance(asiento, Asiento)):
                contador += 1
        return contador

    def verificarIntegridad(self):
        for asiento in self.asientos:
            if (isinstance(asiento, Asiento) and (asiento.registro != self.registro)):
                return "Las piezas no son originales"


        if ((self.registro) != (self.motor.registro)):
            return "Las piezas no son originales"
        
        return "Auto original"

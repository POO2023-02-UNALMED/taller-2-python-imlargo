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
    
    Auto("model 3", 33000, list(),"tesla", Motor(4, "electrico", 142), 341)


    def __init__(self, modelo, precio, asientos, marca, motor, cantidadCreados):
        Auto.cantidadCreados = cantidadCreados
        self.modelo
        self.precio
        self.asientos
        self.marca
        self.motor
    
    def cantidadAsientos(self):
        contador = 0
        for asiento in self.asientos:
            if (isinstance(asiento, Asiento)):
                contador += 1
        return contador

    def verificarIntegridad(self):
        for asiento in self.asientos:
            if (not isinstance(asiento, Asiento)):
                return "Las piezas no son originales"


        if ((self.registro) != (self.motor.registro)):
            return "Las piezas no son originales"
        
        return "Auto original"

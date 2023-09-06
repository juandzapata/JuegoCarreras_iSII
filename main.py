from Controladores.ControladorCarrera import ControladorCarrera
from Clases.vehiculos import Vehiculo
from Clases.vehiculos.Carro import Carro
from Clases.vehiculos.Moto import Moto
from Clases.vehiculos.Karts import Kart
from Clases.Pista import Pista

# Creación de los vehiculos
v1 = Carro("BMW", "i7", 2022, 3000, True, 2)
v2 = Moto("Honda", "Fireblade sp1", "2018", 1100, 80)
v3 = Kart("Suzuki", "Mario Bross Kart", 2005, 300, 120)

# Creación de la pista
pista = Pista(5,200,'Pavimento')

# Inicialización de la lista
vehiculos = [v1, v2, v3]

# Cración del controlador de la carrera
controlador = ControladorCarrera(vehiculos, pista)

# Inicio de la carrera
controlador.iniciar_carrera()

# Resultados de la carrera
resultados = controlador.mostrar_resultados()

for vehiculo, tiempo in resultados:
    print(f'\n{vehiculo} Tiempo en pista: {tiempo} minutos')

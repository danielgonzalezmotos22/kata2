from robot import Robot

walle = Robot()

def test_posicion_inicial():
    assert walle.getdireccion() == "N"


def test_variar_direccion():
    posicion_inicial = walle.getposicion()
    walle.mover("l")

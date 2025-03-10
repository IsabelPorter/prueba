from random import choice

dinero_panel={"jugador1":0,"jugador2":0,"jugador3":0} #dinero que llevas en el panel
#si no resuelves no te llevas el dinero
dinero_total={"jugador1":0,"jugador2":0,"jugador3":0} #dinero acumulado al acabar el panel

def bancarrota():
    print("Pierdes todo tu dinero!")

def pasa_el_turno():
    print("Pasas el turno!")

def tirar_de_la_ruleta():
    gajos= ["25","50","75","100","150","200","300","bancarrota","pasa_el_turno"]
    resultado=choice(gajos)
    return resultado

def tiro_resultado():
    if tirar_de_la_ruleta()=="bancarrota":
        bancarrota()
    elif tirar_de_la_ruleta()=="pasa_el_turno":
        pasa_el_turno()
    else:
        return tirar_de_la_ruleta()
    
def turno():
    tirar_de_la_ruleta()
    tiro_resultado()

def resolver(letra):
    print("")


def main():
    print("")

    

from time import gmtime, strftime


def avisaHorario():
    hora = strftime('%H', gmtime())
    if(hora >= 19):
        print('Es hora de ir a casa')
    else:
        restante = 19 - hora
        print('Aún quedan '+restante+'horas')

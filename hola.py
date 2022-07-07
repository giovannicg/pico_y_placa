from datetime import datetime, time


digito_placa={
    1: 0,
    2: 0,
    3: 1,
    4: 1,
    5: 2,
    6: 2,
    7: 3,
    8: 3,
    9: 4,
    0: 4
}

horario_restriccion = [
    {'inicio': time(7,0,0),
    'fin': time(9,30,0)},
    
    {'inicio': time(16,0,0),
    'fin': time(19,30,0)}
]

def chek_picoyplaca(placa:str, fecha:datetime):
    val = False
    if(len(placa) == 7):
        ultimo_digito = int(placa[-1])
        if chek_placa(ultimo_digito,fecha):
            val= chek_horario(fecha)
    return val
            

def chek_horario (fecha:datetime):
    val = False
    for h in horario_restriccion:
        if fecha.time() > h['inicio']:
            if fecha.time() < h['fin']:
                val = True
    return val
             
def chek_placa(digito:int,fecha:datetime):
    return (digito_placa[digito] == fecha.weekday())


print(chek_picoyplaca('abc1231',datetime(2022,7,4,9,39,0)))

from datetime import datetime, time

# first column: Last digit of the plate
# second column: Dia de la semana "0" = Monday, "1" = Tuesday, "2" = Wednesday, "3" = Thursday, "4" = Friday
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

# restriccion time during Pico Y Placa
horario_restriccion = [
    {'inicio': time(7,0,0),
    'fin': time(9,30,0)},
    
    {'inicio': time(16,0,0),
    'fin': time(19,30,0)}
]

# main function to check if the car is allowed to drive or not
# return True if the car is in Pico y Placa time
def chek_picoyplaca(placa:str, fecha:datetime):
    val = False
    if(len(placa) == 7):
        ultimo_digito = int(placa[-1])
        if chek_placa(ultimo_digito,fecha):
            val = chek_horario(fecha)
    else :
        print("The plate had to have  7 digits")
        return False

    return val
            
# check if the date input is in the range of the restriction
def chek_horario (fecha:datetime):
    val = False
    for h in horario_restriccion:
        if fecha.time() > h['inicio']:
            if fecha.time() < h['fin']:
                val = True
    return val

# check if the last digit of the plate match with the day of the week            
def chek_placa(digito:int,fecha:datetime):
    return (digito_placa[digito] == fecha.weekday())








from datetime import date
from datetime import datetime

#Día actual
today = date.today()

#Fecha actual
now = datetime.now()


def esBisiesto (year):
    if year%4 == 0:
        return True
    


if esBisiesto(today.year):
    print("El año actual {} es bisiesto.".format(today.year))
else:
    print("El año actual {} no es bisiesto.".format(today.year))
    


while (1==1):
    year = int(input("Si desea consultar otro año, introduzcalo a continuación:\n"))
    if esBisiesto(year):
        print("El año {} es bisiesto.".format(year))
    else:
        print("El año {} no es bisiesto.".format(year))

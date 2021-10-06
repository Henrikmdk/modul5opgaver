import math

x = 0
hrs = 0
salary = 0

def stoerste_tal(*tal):
    return max(tal)


def luk_ned(ordre):
    ordre_low = ordre.lower()
    if ordre_low == "ja":
        return "Lukker ned"
    elif ordre_low == "nej":
        return "Afbryder nedlukning"
    else:
        return "Ikke forstået"


def kvadrat(tal):
    return math.sqrt(tal)


def afstand_fra_nul(tal):
    if type(tal) == int or type(tal) == float:
        return abs(tal)
    else:
        return "Kom igen!"


def beregn_løn(timer, lønsats):
    ordinær_arb = 37
    overarbejde = float(timer) - float(ordinær_arb)
    if overarbejde > 0:
        return (float(timer)*float(lønsats))+((float(timer)-37)*1.5)
    else:
        return float(timer)*float(lønsats)


def hotelomkostninger(antal_nætter):
    pris = 795
    return pris*antal_nætter


def flyomkostninger(bynavn):
    priser = \
        {"Stockholm": 2528,
         "Oslo": 2656,
         "Helsinki": 3093,
         "Nuuk": 13462}
    for key, pris in priser.items():
        if key == bynavn.title():
            return pris
        else:
            return "Ukendt destination"


def billejeomkostninger(antal_dage):
    if antal_dage >= 3:
        return (int(antal_dage)*600)-300
    elif antal_dage >= 7:
        return int(antal_dage)*600
    else:
        return (int(antal_dage)*600)-750


def rejseomkostninger(bynavn, antal_dage):
    hotelomk = hotelomkostninger(antal_dage)
    flyomk = flyomkostninger(bynavn)
    bilomk = billejeomkostninger(antal_dage)

    return hotelomk + flyomk + bilomk


def kubik(tal):
    return tal*tal*tal


def deleligt_med_tre(tal):
    if tal%3 == 0:
        return kubik(tal)
    else:
        return False


def increment():
    global x
    x += 1


def g(x, y=4, z=0):
    return 2*x + y + z


def talbehandling(heltal, mult_int=5, skift_fortegn=False):
    if skift_fortegn:
        return (heltal*mult_int)*-1
    else:
        return (heltal * mult_int)


def taxibon(nat, afstand, tid):
    if nat:
        return 44 + (afstand * 10.7) + (tid * 8)
    else:
        return 33 + (afstand * 9) + (tid * 6.3)


# print(stoerste_tal(-1, 12, 200, -100000, 12431435))
# print(luk_ned("Ja"))
# print(luk_ned("Nej"))
# print(luk_ned("Måske"))
# print(kvadrat(3125))
# print(afstand_fra_nul(-1000))

# hrs = input("Indtast dine timer")
# salary = input("Indtast din løn")
# print(beregn_løn(hrs, salary))

# print(rejseomkostninger("Stockholm", 12))

# print(deleligt_med_tre(9))

# increment()
# print(x)

# print(g(3))
# print(g(3, 2))
# print(g(3, 2, 1))

# print(talbehandling(12,skift_fortegn=True))

# print(taxibon(False, 10, 12))
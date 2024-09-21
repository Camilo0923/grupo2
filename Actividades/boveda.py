"""
operadores logicos 

Y -> and
o -> or
no -> not

las reglas de and (y) 
p and q resultado (Las dos condiciones deben ser verdaderas)
v     v = v
v     f = f
f     v = f
f     f = f

las reglas de or(o)
p or q resultado (Cualquiera de las dos condiciones deben ser verdaras)
v    v = v
v    f = v
f    v = v
f    f = f

1 escenario: 35 años de juan es menor< de 35 50 años de pedro < 50 sumaedad = 85 nietos 2
2 escenario: 36 alos de juan 40 años de pedro nietos 3
3 escenario: 24 años de juan 60 años de pedro nietos 0
"""

edadjuan = int(input("ingrese edad de juan "))
edadpedro = int(input("ingrese la edad de pedro "))
nietos = int(input("Ingrese la cantidad de nietos "))
sumaEdad = edadjuan = edadpedro
#1        f    or  v = v             and     f               and     v
#2        v    or  c = v             and     v               and     v
#3        f    or  f   f             and     v               and     f 
if (edadjuan > 35 or edadpedro < 50) and (sumaEdad % 2 == 0) and (nietos >= 1):
    print ("Tienen acceso a la boveda")
else:
    print("no tiene acceso a a boveda")
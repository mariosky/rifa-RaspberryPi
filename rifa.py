# -*- coding: utf-8 -*-
__author__ = 'mariosky'

participantes = (
    ("Chriss", 16    ),
    ("Chuy Facking ", 18    ),
    ("Arturo", 19    ),
    ("ICarlos", 15    ),
    ("Frank", 10    ),
    ("Alberto", 10    ),
    ("Data", 16    ),
    ("Abraham", 17    ),
    ("Antonio", 26    ),
    ("Alejandra", 13    ),
    ("Xochilt", 14    ),
    ("Ivan", 6    ),
    ("Josefina", 9    ),
    ("Leonardo", 11    ),
    ("Omar A.", 6    ),
    ("Juan", 8    ),
    ("Camilo", 5    ),
    ("Alan", 6    ),
    ("Ing", 1    ),
    ("Gabriel", 1    ),
    ("Omar", 1    ),
    ("Ricardo", 1    ),
    ("Jose Carlos", 12    ),
    ("Ricardo", 1    ),
    ("Marthys", 11    ),
    ("Arturo", 1    ),
    ("Daniel", 1    ),
    ("Carlos", 1    ),
    ("Cinthya", 1    ),
    ("Luciana", 1    ),
    ("Gustavo", 1    ),
    ("Victor", 1    ),
    ("Luis Rodriguez", 13    ),
    ("Tano  Barraza", 13    ),
    ("Samuel", 6    ),
    ("Cristian V	", 5    ),
    ("Jose", 11    ),
    ("Shuy Rz", 11    ),
    ("Marco Acr", 1    ),
    ("Ivan", 5    ),
    ("Gil", 5 ),
)

def genera_boletos(participante):
    return [participante[0] for x in range(participante[1])]

boletos = []
for participante in participantes:
    boletos.extend(genera_boletos(participante))

import random

print u"¡Al quinto boleto, los boletos se reinsertan!"

for i in range(4):
    print random.choice(boletos), u"No Ganó"

print random.choice(boletos), "GANADOR"




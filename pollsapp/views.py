from django.shortcuts import render
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login
from .models import Empleado
from .models import Pregunta
from .templates import *
from django.http.response import HttpResponse


def inicio(request):
    return render(request,'home.html')

def respuesta(request):

    p1 = int(request.POST["condicion11"])
    p2 = int(request.POST["condicion12"])
    p3 = int(request.POST["condicion13"])
    p4 = int(request.POST["condicion14"])
    p5 = int(request.POST["condicion15"])
    p6 = int(request.POST["condicion16"])

    
    condiciones2=(p1+p2+p3+p4+p5+p6)/6

    p11 = int(request.POST["cooperacion11"])
    p12 = int(request.POST["cooperacion12"])
    p13 = int(request.POST["cooperacion13"])
    p14 = int(request.POST["cooperacion14"])
    p15 = int(request.POST["cooperacion15"])
    p16 = int(request.POST["cooperacion16"])
    p17 = int(request.POST["cooperacion17"])

    cooperacion2=(p11+p12+p13+p14+p15+p16+p17)/7

    p21 = int(request.POST["supervicion11"])
    p22 = int(request.POST["supervicion12"])
    p23 = int(request.POST["supervicion13"])
    p24 = int(request.POST["supervicion14"])
    p25 = int(request.POST["supervicion15"])
    p26 = int(request.POST["supervicion16"])
    p27 = int(request.POST["supervicion17"])

    supervision2=(p21+p22+p23+p24+p25+p26+p27)/7

    p31 = int(request.POST["fisica11"])
    p32 = int(request.POST["fisica12"])
    p33 = int(request.POST["fisica13"])
    p34 = int(request.POST["fisica14"])
    p35 = int(request.POST["fisica15"])
    p36 = int(request.POST["fisica16"])
    p37 = int(request.POST["fisica17"])
  

    condicionesfisicas2=(p31+p32+p33+p34+p35+p36+p37)/7

    p41 = int(request.POST["p41"])
    p42 = int(request.POST["p42"])
    p43 = int(request.POST["p43"])
    p44 = int(request.POST["p44"])
    p45 = int(request.POST["p45"])
    p46 = int(request.POST["p46"])
    p47 = int(request.POST["p47"])

    satisfaccion2=(p41+p42+p43+p44+p45+p46+p47)/7

    p51 = int(request.POST["p51"])
    p52 = int(request.POST["p52"])
    p53 = int(request.POST["p53"])
    p54 = int(request.POST["p54"])
    p55 = int(request.POST["p55"])

    participacion2=(p51+p52+p53+p54+p55)/5
    
    resultados=Pregunta(condiciones=condiciones2,cooperacion=cooperacion2,supervision=supervision2,
    condicionesfisicas=condicionesfisicas2,satisfaccion=satisfaccion2,participacion=participacion2)

    resultados.save()

    return render(request,'home.html')
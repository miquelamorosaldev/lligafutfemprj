from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Lliga, Jugadora, Equip, Partit, Event
from django.urls import reverse
import matplotlib.pyplot as plt
from io import BytesIO
import base64

# Objecte per guardar les lligues
lligues = []

def index(request):
    lligues = Lliga.objects.all()
    #print(lligues)
    return render(request, 'lliga/index.html', {'lligues': lligues})


def detail(request, lliga_id):
    #lliga = get_object_or_404(Lliga, pk=lliga_id)
    lliga = Lliga.objects.first()
    if lliga_id:
        lliga = Lliga.objects.get(pk=lliga_id)
    
    equips = lliga.equips.all()
    #print("equips", equips)
    return render(request, "lliga/detail.html", {"lliga": lliga, "equips": equips})

def grafic_golejadores(plt):
	buffer = BytesIO()
	plt.savefig(buffer, format='png')
	buffer.seek(0)
	image_png = buffer.getvalue()
	buffer.close()

	graphic = base64.b64encode(image_png)
	graphic = graphic.decode('utf-8')
	return graphic


def golejadores(request, equip_id):
    # golejadores:list[str] = []
    equip = get_object_or_404(Equip, pk=equip_id)
    print("equip", equip)
    jugadores = Jugadora.objects.filter(equip=equip).order_by('dorsal')
    print(jugadores)
    golejadores = dict()
    # Info per generar un gràfic.
    noms_jugadores = []
    gols_jugadores = []
    for jugadora in jugadores:
        gols_jugadora = Event.objects.filter(equip=equip, jugador=jugadora, tipus=Event.EventType.GOL).count()
        if(gols_jugadora>5):
            golejadores[jugadora.nom]=gols_jugadora
            golejadores[jugadora.nom]=gols_jugadora
            noms_jugadores.append(jugadora.nom)
            gols_jugadores.append(gols_jugadora)

    golejadores_ord = sorted(golejadores.items(), key=lambda x:x[1], reverse=True)
    golejadores_final = dict(golejadores_ord)

    plt.bar(range(len(gols_jugadores)), gols_jugadores, tick_label=noms_jugadores)
    grafic = grafic_golejadores(plt)

    #jugadores = ["a","b","c"]
    return render(request, "lliga/golejadores.html", {"equip": equip, "jugadores": golejadores_final, "grafic": grafic})


def equip_detail(request, equip_id):
    equip = get_object_or_404(Equip, pk=equip_id)
    print("equip", equip)
    jugadores = Jugadora.objects.filter(equip=equip).order_by('dorsal')
    #jugadores = ["a","b","c"]
    print(jugadores)
    return render(request, "lliga/equip_detail.html", {"equip": equip, "jugadores": jugadores})


def classificacio(request,lliga_id=None):
    lliga = Lliga.objects.first()
    if lliga_id:
        lliga = Lliga.objects.get(pk=lliga_id)
    equips = lliga.equips.all()
    classi = []

    # calculem punts en llista de tuples (equip,punts)
    for equip in equips:
        punts = 0
        for partit in lliga.partit_set.filter(local=equip):
            if partit.gols_local() > partit.gols_visitant():
                punts += 3
            elif partit.gols_local() == partit.gols_visitant():
                punts += 1
        for partit in lliga.partit_set.filter(visitant=equip):
            if partit.gols_local() < partit.gols_visitant():
                punts += 3
            elif partit.gols_local() == partit.gols_visitant():
                punts += 1
        classi.append( (punts,equip.nom) )
    # ordenem llista
    classi.sort(reverse=True)
    return render(request,"lliga/classificacio.html",
                {
                    "lliga":lliga,
                    "classificacio":classi,
                })
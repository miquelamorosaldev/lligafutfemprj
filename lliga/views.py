from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Lliga, Jugadora, Equip, Partit, Event
from django.urls import reverse

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

def equip_detail(request, equip_id):
    equip = get_object_or_404(Equip, pk=equip_id)
    print("equip", equip)
    jugadores = Jugadora.objects.filter(equip=equip).order_by('dorsal')
    #jugadores = ["a","b","c"]
    print(jugadores)
    return render(request, "lliga/equip_detail.html", {"equip": equip, "jugadores": jugadores})

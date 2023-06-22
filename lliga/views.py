from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Lliga, Jugadora, Equip, Partit, Event
from django.urls import reverse


def index(request):
    lligues = Lliga.objects.all()
    #print(lligues)
    return render(request, 'lliga/index.html', {'lligues': lligues})

def detail(request, lliga_id):
    lliga = get_object_or_404(Lliga, pk=lliga_id)
    equips = Equip.objects.filter(lliga=lliga)
    print(equips)
    return render(request, "lliga/detail.html", {"lliga": lliga, "equips": equips})

from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from faker import Faker
import datetime
#import time
from random import randint, sample
 
from lliga.models import *
 
faker = Faker(["es_CA","es_ES"])
Num_Jugadores_Equip: int = 20
 
class Command(BaseCommand):
    help = 'Crea una lliga amb equips i jugadors'
 
    def add_arguments(self, parser):
        parser.add_argument('titol_lliga', nargs=1, type=str)
 
    def handle(self, *args, **options):
        #print(jugador=Jugadora.objects.get(dorsal=5))
        titol_lliga = options['titol_lliga'][0]
        lliga = Lliga.objects.filter(nom_temporada=titol_lliga)
        if lliga.count()>0:
            print("Aquesta lliga ja està creada. Posa un altre nom.")
            return
 
        print("Creem la nova lliga: {}".format(titol_lliga))
        lliga = Lliga(nom_temporada=titol_lliga)
        lliga.save()
 
        print("Creem equips amb Faker.")
        prefixos = ["CD", "Athletic", "", "Deportivo", "Unión Deportiva", "FC", "Esportiu", "Balompié", "Futbol", "Polideportivo"]
        for i in range(16):
            ciutat = faker.city()
            prefix = prefixos[randint(0,len(prefixos)-1)]
            if prefix:
                prefix += " "
            nom =  prefix + ciutat
            equip = Equip(ciutat=ciutat,nom=nom)
            #print(equip)
            equip.save()
            lliga.equips.add(equip)
        
        # print("Creem equips, des de l'Open Data")


            # Seleccionarem algunes jugadores golejadores.
            print("Creem jugadores de l'equip "+nom)
            for j in range(Num_Jugadores_Equip):
                nom = faker.first_name_female()
                cognom = faker.last_name()
                jugadora = Jugadora(nom=nom,cognom=cognom,dorsal=j,equip=equip)
                #print(jugador)
                jugadora.save()
 
        print("Creem partits de la lliga")

        for local in lliga.equips.all():
            for visitant in lliga.equips.all():
                if local!=visitant:
                    partit = Partit(local=local,visitant=visitant)
                    partit.local = local
                    partit.visitant = visitant
                    partit.lliga = lliga
                    partit.save()
                    num_gols_local = randint(0,7)
                    num_gols_vis = randint(0,7)
                    #partit,temps,tipus,jugador,equip,jugador2,detalls

                    #print("Creem els events: gols, targetes... de cada partit.")
                    num_gols_local = randint(0,7)
                    num_gols_vis = randint(0,7)
                    # generem llista dorsals de les jugadores que faran gols.
                    jug_gols_loc = sample(range(1, Num_Jugadores_Equip), num_gols_local)
                    jug_gols_vis = sample(range(1, Num_Jugadores_Equip), num_gols_vis)

                    for m in range(num_gols_local):
                        #print(jug_gols_loc[m])
                        jugadora=Jugadora.objects.filter(dorsal=jug_gols_loc[m],equip=local)[0]
                        event = Event(partit=partit,temps=datetime.time(),tipus=Event.EventType.GOL,equip=local,jugador=jugadora)
                        event.save()
                    for n in range(num_gols_vis):
                        #print(jug_gols_vis[n])
                        jugadora=Jugadora.objects.filter(dorsal=jug_gols_vis[n],equip=visitant)[0]
                        event = Event(partit=partit,temps=datetime.time(),tipus=Event.EventType.GOL,equip=visitant,jugador=jugadora)
                        event.save()
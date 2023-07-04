rom faker import Faker
from django.utils import timezone
from datetime import timedelta, time
from random import randint

faker = Faker(['es_ES', 'es_CA'])

print("Creem equips")
prefixos = ["CD", "Athletic", "Rayo", "FC", "Deportivo", "Unión Deportiva", "Balonpié"]
for i in range(20):
    ciutat = faker.city()
    prefix = prefixos[randint(0,len(prefixos)-1)]
    if prefix:
        prefix += " "
    nom = str(i) + ' ' + prefix + ' ' + ciutat
    # equip = Equip(ciutat=ciutat,nom=nom)
    print(nom)
    #print(equip)
    print("Creem jugadores de l'equip "+nom)
    for j in range(25):
        dorsal = str(j)
        nom = faker.first_name_female()
        cognom1 = faker.last_name()
        cognom2 = faker.last_name()
        print(i, ' - ', nom, ' ' ,cognom1)

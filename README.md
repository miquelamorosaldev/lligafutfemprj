# lligafutfemprj

Exemple de web creada amb Python i Django; és una [web per gestionar lligues de futbol femení, exemple proposat a bytes.cat](https://www.bytes.cat/django_lliga) 

## Instruccions arrencar el projecte:
````sh
(env) nomusuari@linux:~/lligafemprj$ ./manage.py runserver
```

## Instruccions per a crear una superusuaria i accedir al panell d'admin:
````sh
(env) nomusuari@linux:~/lligafemprj$ python manage.py createsuperuser
(env) nomusuari@linux:~/lligafemprj$ firefox https://localhost:8000/admin
```

## Instruccions seeder:
Aquesta instrucció crea una lliga (si no existeix) amb el nom que indiquem al paràmetre <nom_lliga>.
Genera aleatòriament jugadores, partits i events de partits (gols, targetes...)
```sh
(env) nomusuari@linux:~/lligafemprj$ ./manage.py crea_lliga <nom_lliga>
```

## Control versions (manual) projecte:

### v2.
- El seeder ja crea partits i es creen els resultats a partir d'events de GOL.
- A més a més, [s'obté llista d'equips a partir de dades obertes.]()
- La classificació de la lliga ja funciona.

### v1.
- Primera versió executable: gestió de jugadores, equips i lligues completa.
- El seeder està incomplet: falten partits i events.
- Falten les pàgines més importants: partits i classificació.

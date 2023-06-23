from django.db import models

# Observació: Django genera per defecte camps id autonumèrics
# com a clau primària. Hi ha formes de canviar aquest 
# comportament però per ara ens sembla OK.

# Hauria de posar una relació ManyToMany per tal que un mateix equip
# pugui compatir en diverses lligues en un any (Champions)
# equips = models.ManyToManyField(Equip)
class Equip(models.Model):
    nom_equip = models.CharField(max_length=100)
    ciutat = models.CharField(max_length=100)
    estadi = models.CharField(max_length=100)
    #lliga = models.ForeignKey(Lliga, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom_equip
        

class Lliga(models.Model):
    nom_temporada = models.CharField(max_length=100)
    equips = models.ManyToManyField(Equip)
    def __str__(self):
        return self.nom_temporada


class Jugadora(models.Model):
    nom = models.CharField(max_length=100)
    cognom = models.CharField(max_length=100)
    dorsal = models.IntegerField()
    equip = models.ForeignKey(Equip, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.dorsal} - {self.nom}'
    class Meta:
        verbose_name_plural = 'Jugadores'

class Partit(models.Model):
    equip_local = models.ForeignKey(Equip, related_name='equip_local', on_delete=models.CASCADE)
    equip_visitant = models.ForeignKey(Equip, related_name='equip_visitant', on_delete=models.CASCADE)
    # Solució subòptima i provisional.
    # Els gols són un event associat al partit, és necessari per a registrar
    gols_locals = models.IntegerField()
    gols_visitants = models.IntegerField()
    data_partit = models.DateField()
    lliga = models.ForeignKey(Lliga, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.equip_local} vs {self.equip_visitant}'

class Event(models.Model):
    partit = models.ForeignKey(Partit, on_delete=models.CASCADE)
    # Solució subòptima i provisional.
    tipus_event = models.CharField(max_length=100)
    partit = models.ForeignKey(Partit,on_delete=models.CASCADE)
    temps = models.TimeField(auto_now=False, auto_now_add=False)
    jugadora = models.ForeignKey(Jugadora,null=True,
        on_delete=models.SET_NULL, related_name="events_fets")

    def __str__(self):
        return f'{self.tipus_event} - minut {self.minut}'
from django.db import models

# Observació: Django genera per defecte camps id autonumèrics
# com a clau primària. Hi ha formes de canviar aquest 
# comportament però per ara ens sembla OK.

class Lliga(models.Model):
    nom_temporada = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_temporada
    class Meta:
        verbose_name_plural = 'Lliga'


class Equip(models.Model):
    nom_equip = models.CharField(max_length=100)
    ciutat = models.CharField(max_length=100)
    estadi = models.CharField(max_length=100)
    lliga = models.ForeignKey(Lliga, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_equip

class Jugadora(models.Model):
    nom = models.CharField(max_length=100)
    cognom = models.CharField(max_length=100)
    dorsal = models.IntegerField()
    equip = models.ForeignKey(Equip, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nom} {self.cognom}'

class Partit(models.Model):
    equip_local = models.ForeignKey(Equip, related_name='partits_local', on_delete=models.CASCADE)
    equip_visitant = models.ForeignKey(Equip, related_name='partits_visitant', on_delete=models.CASCADE)
    gols_locals = models.IntegerField()
    gols_visitants = models.IntegerField()
    data_partit = models.DateField()

    def __str__(self):
        return f'{self.equip_local} vs {self.equip_visitant}'

class Event(models.Model):
    partit = models.ForeignKey(Partit, on_delete=models.CASCADE)
    tipus_event = models.CharField(max_length=100)
    minut = models.IntegerField()

    def __str__(self):
        return f'{self.tipus_event} - minut {self.minut}'
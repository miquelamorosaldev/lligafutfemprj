from django.db import models

# Observació: Django genera per defecte camps id autonumèrics
# com a clau primària. Hi ha formes de canviar aquest 
# comportament però per ara ens sembla OK.

# Hauria de posar una relació ManyToMany per tal que un mateix equip
# pugui compatir en diverses lligues en un any (Champions)
# equips = models.ManyToManyField(Equip)
class Equip(models.Model):
    nom = models.CharField(max_length=100)
    ciutat = models.CharField(max_length=100,null=True)
    estadi = models.CharField(max_length=100,null=True)
    #lliga = models.ForeignKey(Lliga, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom


class Lliga(models.Model):
    nom_temporada = models.CharField(max_length=100)
    equips = models.ManyToManyField(Equip)
    def __str__(self):
        return self.nom_temporada
    class Meta:
        verbose_name_plural = 'Lligues'


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
    class Meta:
        unique_together = ["local","visitant","lliga"]
    local = models.ForeignKey(Equip,on_delete=models.CASCADE,
                    related_name="partits_local",null=True,blank=True)
    visitant = models.ForeignKey(Equip,on_delete=models.CASCADE,
                    related_name="partits_visitant",null=True,blank=True)
    lliga = models.ForeignKey(Lliga,on_delete=models.CASCADE)
    detalls = models.TextField(null=True,blank=True)
    inici = models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return "{} - {}".format(self.local,self.visitant)
    def gols_local(self):
        return self.event_set.filter(
            tipus=Event.EventType.GOL,equip=self.local).count()
    def gols_visitant(self):
        return self.event_set.filter(
            tipus=Event.EventType.GOL,equip=self.visitant).count()


class Event(models.Model):
    # Solució subòptima i provisional.
    # tipus_event = models.CharField(max_length=100)
    # el tipus d'event l'implementem amb algo tipus "enum"
    class EventType(models.TextChoices):
        GOL = "GOL"
        AUTOGOL = "AUTOGOL"
        FALTA = "FALTA"
        PENALTY = "PENALTY"
        MANS = "MANS"
        CESSIO = "CESSIO"
        FORA_DE_JOC = "FORA_DE_JOC"
        ASSISTENCIA = "ASSISTENCIA"
        TARGETA_GROGA = "TARGETA_GROGA"
        TARGETA_VERMELLA = "TARGETA_VERMELLA"
    partit = models.ForeignKey(Partit,on_delete=models.CASCADE)
    temps = models.TimeField()
    tipus = models.CharField(max_length=30,choices=EventType.choices)
    jugador = models.ForeignKey(Jugadora,null=True,
                    on_delete=models.SET_NULL,
                    related_name="events_fets")
    equip = models.ForeignKey(Equip,null=True,
                    on_delete=models.SET_NULL)
    # per les faltes
    jugador2 = models.ForeignKey(Jugadora,null=True,blank=True,
                    on_delete=models.SET_NULL,
                    related_name="events_rebuts")
    detalls = models.TextField(null=True,blank=True)
    def __str__(self):
        return f'{self.EventType} - {self.jugador}'
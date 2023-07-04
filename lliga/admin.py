from django.contrib import admin

# Register your models here.

from .models import *

class LligaAdmin(admin.ModelAdmin):
    filter_horizontal = ["equips"]
admin.site.register(Lliga,LligaAdmin)

admin.site.register(Equip)
admin.site.register(Jugadora)


class EventInline(admin.TabularInline):
	model = Event
	fields = ["temps","tipus","jugador","equip"]
	

class PartitAdmin(admin.ModelAdmin):
        # podem fer cerques en els models relacionats
        # (noms dels equips o títol de la lliga)
    search_fields = ["local__nom","visitant__nom","lliga__titol"]
        # el camp personalitzat ("resultats" o recompte de gols)
        # el mostrem com a "readonly_field"
    readonly_fields = ["resultat",]
    list_display = ["local","visitant","resultat","lliga","inici"]
    ordering = ("-inici",)
    inlines = [EventInline,]
    def resultat(self,obj):
        gols_local = obj.event_set.filter(
                        tipus=Event.EventType.GOL,
                                equip=obj.local).count()
        gols_visit = obj.event_set.filter(
                        tipus=Event.EventType.GOL,
                                equip=obj.visitant).count()
        return "{} - {}".format(gols_local,gols_visit)

admin.site.register(Partit,PartitAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ["partit","temps","tipus","equip","jugador"]

admin.site.register(Event,EventAdmin)
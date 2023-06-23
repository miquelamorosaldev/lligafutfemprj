from django.contrib import admin
from .models import Lliga, Equip, Jugadora, Partit, Event

#class QuestionAdmin(admin.ModelAdmin):
#    fields = ["pub_date", "question_text"]

admin.site.register(Lliga)
admin.site.register(Equip)
admin.site.register(Jugadora)
admin.site.register(Partit)
admin.site.register(Event)

# Panells personalitzats.
